from __future__ import annotations

from abc import ABC
from typing import Callable
from typing import ClassVar
from typing import Final
from typing import Generic
from typing import Tuple
from typing import TypeVar
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

T = TypeVar("T")

class EventType(Generic[T]):
    def __iadd__(self, other: T): ...
    def __isub__(self, other: T): ...

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

class InternalResources(ABC, Object):
    """"""

    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def GetHashCode(self) -> int:
        """

        :return:
        """
    def GetType(self) -> Type:
        """

        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """

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

class SerialData(Enum):
    """"""

    Chars: SerialData = ...
    """"""
    Eof: SerialData = ...
    """"""

class SerialDataReceivedEventArgs(EventArgs):
    """"""

    @property
    def EventType(self) -> SerialData:
        """

        :return:
        """
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def GetHashCode(self) -> int:
        """

        :return:
        """
    def GetType(self) -> Type:
        """

        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """

SerialDataReceivedEventHandler: Callable[[object, SerialDataReceivedEventArgs], None] = ...
"""

:param sender: 
:param e: 
"""

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

class SerialErrorReceivedEventArgs(EventArgs):
    """"""

    @property
    def EventType(self) -> SerialError:
        """

        :return:
        """
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def GetHashCode(self) -> int:
        """

        :return:
        """
    def GetType(self) -> Type:
        """

        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """

SerialErrorReceivedEventHandler: Callable[[object, SerialErrorReceivedEventArgs], None] = ...
"""

:param sender: 
:param e: 
"""

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

class SerialPinChangedEventArgs(EventArgs):
    """"""

    @property
    def EventType(self) -> SerialPinChange:
        """

        :return:
        """
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def GetHashCode(self) -> int:
        """

        :return:
        """
    def GetType(self) -> Type:
        """

        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """

SerialPinChangedEventHandler: Callable[[object, SerialPinChangedEventArgs], None] = ...
"""

:param sender: 
:param e: 
"""

class SerialPort(Component, IComponent, IDisposable):
    """"""

    InfiniteTimeout: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    @overload
    def __init__(self):
        """"""
    @overload
    def __init__(self, container: IContainer):
        """

        :param container:
        """
    @overload
    def __init__(self, portName: str):
        """

        :param portName:
        """
    @overload
    def __init__(self, portName: str, baudRate: int):
        """

        :param portName:
        :param baudRate:
        """
    @overload
    def __init__(self, portName: str, baudRate: int, parity: Parity):
        """

        :param portName:
        :param baudRate:
        :param parity:
        """
    @overload
    def __init__(self, portName: str, baudRate: int, parity: Parity, dataBits: int):
        """

        :param portName:
        :param baudRate:
        :param parity:
        :param dataBits:
        """
    @overload
    def __init__(
        self, portName: str, baudRate: int, parity: Parity, dataBits: int, stopBits: StopBits
    ):
        """

        :param portName:
        :param baudRate:
        :param parity:
        :param dataBits:
        :param stopBits:
        """
    @property
    def BaseStream(self) -> Stream:
        """

        :return:
        """
    @property
    def BaudRate(self) -> int:
        """

        :return:
        """
    @BaudRate.setter
    def BaudRate(self, value: int) -> None: ...
    @property
    def BreakState(self) -> bool:
        """

        :return:
        """
    @BreakState.setter
    def BreakState(self, value: bool) -> None: ...
    @property
    def BytesToRead(self) -> int:
        """

        :return:
        """
    @property
    def BytesToWrite(self) -> int:
        """

        :return:
        """
    @property
    def CDHolding(self) -> bool:
        """

        :return:
        """
    @property
    def Container(self) -> IContainer:
        """

        :return:
        """
    @property
    def CtsHolding(self) -> bool:
        """

        :return:
        """
    @property
    def DataBits(self) -> int:
        """

        :return:
        """
    @DataBits.setter
    def DataBits(self, value: int) -> None: ...
    @property
    def DiscardNull(self) -> bool:
        """

        :return:
        """
    @DiscardNull.setter
    def DiscardNull(self, value: bool) -> None: ...
    @property
    def DsrHolding(self) -> bool:
        """

        :return:
        """
    @property
    def DtrEnable(self) -> bool:
        """

        :return:
        """
    @DtrEnable.setter
    def DtrEnable(self, value: bool) -> None: ...
    @property
    def Encoding(self) -> Encoding:
        """

        :return:
        """
    @Encoding.setter
    def Encoding(self, value: Encoding) -> None: ...
    @property
    def Handshake(self) -> Handshake:
        """

        :return:
        """
    @Handshake.setter
    def Handshake(self, value: Handshake) -> None: ...
    @property
    def IsOpen(self) -> bool:
        """

        :return:
        """
    @property
    def NewLine(self) -> str:
        """

        :return:
        """
    @NewLine.setter
    def NewLine(self, value: str) -> None: ...
    @property
    def Parity(self) -> Parity:
        """

        :return:
        """
    @Parity.setter
    def Parity(self, value: Parity) -> None: ...
    @property
    def ParityReplace(self) -> int:
        """

        :return:
        """
    @ParityReplace.setter
    def ParityReplace(self, value: int) -> None: ...
    @property
    def PortName(self) -> str:
        """

        :return:
        """
    @PortName.setter
    def PortName(self, value: str) -> None: ...
    @property
    def ReadBufferSize(self) -> int:
        """

        :return:
        """
    @ReadBufferSize.setter
    def ReadBufferSize(self, value: int) -> None: ...
    @property
    def ReadTimeout(self) -> int:
        """

        :return:
        """
    @ReadTimeout.setter
    def ReadTimeout(self, value: int) -> None: ...
    @property
    def ReceivedBytesThreshold(self) -> int:
        """

        :return:
        """
    @ReceivedBytesThreshold.setter
    def ReceivedBytesThreshold(self, value: int) -> None: ...
    @property
    def RtsEnable(self) -> bool:
        """

        :return:
        """
    @RtsEnable.setter
    def RtsEnable(self, value: bool) -> None: ...
    @property
    def Site(self) -> ISite:
        """

        :return:
        """
    @Site.setter
    def Site(self, value: ISite) -> None: ...
    @property
    def StopBits(self) -> StopBits:
        """

        :return:
        """
    @StopBits.setter
    def StopBits(self, value: StopBits) -> None: ...
    @property
    def WriteBufferSize(self) -> int:
        """

        :return:
        """
    @WriteBufferSize.setter
    def WriteBufferSize(self, value: int) -> None: ...
    @property
    def WriteTimeout(self) -> int:
        """

        :return:
        """
    @WriteTimeout.setter
    def WriteTimeout(self, value: int) -> None: ...
    def Close(self) -> None:
        """"""
    def CreateObjRef(self, requestedType: Type) -> ObjRef:
        """

        :param requestedType:
        :return:
        """
    def DiscardInBuffer(self) -> None:
        """"""
    def DiscardOutBuffer(self) -> None:
        """"""
    def Dispose(self) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def GetHashCode(self) -> int:
        """

        :return:
        """
    def GetLifetimeService(self) -> object:
        """

        :return:
        """
    @classmethod
    def GetPortNames(cls) -> Array[str]:
        """

        :return:
        """
    def GetType(self) -> Type:
        """

        :return:
        """
    def InitializeLifetimeService(self) -> object:
        """

        :return:
        """
    def Open(self) -> None:
        """"""
    @overload
    def Read(self, buffer: Array[int], offset: int, count: int) -> int:
        """

        :param buffer:
        :param offset:
        :param count:
        :return:
        """
    @overload
    def Read(self, buffer: Array[Char], offset: int, count: int) -> int:
        """

        :param buffer:
        :param offset:
        :param count:
        :return:
        """
    def ReadByte(self) -> int:
        """

        :return:
        """
    def ReadChar(self) -> int:
        """

        :return:
        """
    def ReadExisting(self) -> str:
        """

        :return:
        """
    def ReadLine(self) -> str:
        """

        :return:
        """
    def ReadTo(self, value: str) -> str:
        """

        :param value:
        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """
    @overload
    def Write(self, text: str) -> None:
        """

        :param text:
        """
    @overload
    def Write(self, buffer: Array[int], offset: int, count: int) -> None:
        """

        :param buffer:
        :param offset:
        :param count:
        """
    @overload
    def Write(self, buffer: Array[Char], offset: int, count: int) -> None:
        """

        :param buffer:
        :param offset:
        :param count:
        """
    def WriteLine(self, text: str) -> None:
        """

        :param text:
        """
    DataReceived: EventType[SerialDataReceivedEventHandler] = ...
    """"""
    Disposed: EventType[EventHandler] = ...
    """"""
    ErrorReceived: EventType[SerialErrorReceivedEventHandler] = ...
    """"""
    PinChanged: EventType[SerialPinChangedEventHandler] = ...
    """"""

class SerialStream(Stream, IDisposable):
    """"""

    @property
    def BreakState(self) -> bool:
        """

        :return:
        """
    @BreakState.setter
    def BreakState(self, value: bool) -> None: ...
    @property
    def CanRead(self) -> bool:
        """

        :return:
        """
    @property
    def CanSeek(self) -> bool:
        """

        :return:
        """
    @property
    def CanTimeout(self) -> bool:
        """

        :return:
        """
    @property
    def CanWrite(self) -> bool:
        """

        :return:
        """
    @property
    def Length(self) -> int:
        """

        :return:
        """
    @property
    def Position(self) -> int:
        """

        :return:
        """
    @Position.setter
    def Position(self, value: int) -> None: ...
    @property
    def ReadTimeout(self) -> int:
        """

        :return:
        """
    @ReadTimeout.setter
    def ReadTimeout(self, value: int) -> None: ...
    @property
    def WriteTimeout(self) -> int:
        """

        :return:
        """
    @WriteTimeout.setter
    def WriteTimeout(self, value: int) -> None: ...
    def BeginRead(
        self, buffer: Array[int], offset: int, count: int, callback: AsyncCallback, state: object
    ) -> IAsyncResult:
        """

        :param buffer:
        :param offset:
        :param count:
        :param callback:
        :param state:
        :return:
        """
    def BeginWrite(
        self, buffer: Array[int], offset: int, count: int, callback: AsyncCallback, state: object
    ) -> IAsyncResult:
        """

        :param buffer:
        :param offset:
        :param count:
        :param callback:
        :param state:
        :return:
        """
    def Close(self) -> None:
        """"""
    @overload
    def CopyTo(self, destination: Stream) -> None:
        """

        :param destination:
        """
    @overload
    def CopyTo(self, destination: Stream, bufferSize: int) -> None:
        """

        :param destination:
        :param bufferSize:
        """
    @overload
    def CopyToAsync(self, destination: Stream) -> Task:
        """

        :param destination:
        :return:
        """
    @overload
    def CopyToAsync(self, destination: Stream, bufferSize: int) -> Task:
        """

        :param destination:
        :param bufferSize:
        :return:
        """
    @overload
    def CopyToAsync(
        self, destination: Stream, bufferSize: int, cancellationToken: CancellationToken
    ) -> Task:
        """

        :param destination:
        :param bufferSize:
        :param cancellationToken:
        :return:
        """
    def CreateObjRef(self, requestedType: Type) -> ObjRef:
        """

        :param requestedType:
        :return:
        """
    def Dispose(self) -> None:
        """"""
    def EndRead(self, asyncResult: IAsyncResult) -> int:
        """

        :param asyncResult:
        :return:
        """
    def EndWrite(self, asyncResult: IAsyncResult) -> None:
        """

        :param asyncResult:
        """
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def Flush(self) -> None:
        """"""
    @overload
    def FlushAsync(self) -> Task:
        """

        :return:
        """
    @overload
    def FlushAsync(self, cancellationToken: CancellationToken) -> Task:
        """

        :param cancellationToken:
        :return:
        """
    def GetHashCode(self) -> int:
        """

        :return:
        """
    def GetLifetimeService(self) -> object:
        """

        :return:
        """
    def GetType(self) -> Type:
        """

        :return:
        """
    def InitializeLifetimeService(self) -> object:
        """

        :return:
        """
    def Read(self, buffer: Array[int], offset: int, count: int) -> Tuple[int, Array[int]]:
        """

        :param buffer:
        :param offset:
        :param count:
        :return:
        """
    @overload
    def ReadAsync(self, buffer: Array[int], offset: int, count: int) -> Task[int]:
        """

        :param buffer:
        :param offset:
        :param count:
        :return:
        """
    @overload
    def ReadAsync(
        self, buffer: Array[int], offset: int, count: int, cancellationToken: CancellationToken
    ) -> Task[int]:
        """

        :param buffer:
        :param offset:
        :param count:
        :param cancellationToken:
        :return:
        """
    def ReadByte(self) -> int:
        """

        :return:
        """
    def Seek(self, offset: int, origin: SeekOrigin) -> int:
        """

        :param offset:
        :param origin:
        :return:
        """
    def SetLength(self, value: int) -> None:
        """

        :param value:
        """
    def ToString(self) -> str:
        """

        :return:
        """
    def Write(self, buffer: Array[int], offset: int, count: int) -> None:
        """

        :param buffer:
        :param offset:
        :param count:
        """
    @overload
    def WriteAsync(self, buffer: Array[int], offset: int, count: int) -> Task:
        """

        :param buffer:
        :param offset:
        :param count:
        :return:
        """
    @overload
    def WriteAsync(
        self, buffer: Array[int], offset: int, count: int, cancellationToken: CancellationToken
    ) -> Task:
        """

        :param buffer:
        :param offset:
        :param count:
        :param cancellationToken:
        :return:
        """
    def WriteByte(self, value: int) -> None:
        """

        :param value:
        """

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
