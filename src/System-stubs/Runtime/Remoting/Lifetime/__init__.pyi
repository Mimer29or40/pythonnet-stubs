"""Automatically generated stubs for C# namespace: System.Runtime.Remoting.Lifetime."""

from typing import overload

from System import Enum
from System import MarshalByRefObject
from System import Object
from System import TimeSpan
from System import Type
from System.Runtime.Remoting import ObjRef
from System.Runtime.Remoting.Contexts import Context
from System.Runtime.Remoting.Contexts import IContextProperty
from System.Runtime.Remoting.Contexts import IContributeObjectSink
from System.Runtime.Remoting.Messaging import IMessage
from System.Runtime.Remoting.Messaging import IMessageCtrl
from System.Runtime.Remoting.Messaging import IMessageSink

class ClientSponsor(MarshalByRefObject, ISponsor):
    """"""
    @overload
    def __init__(self) -> None:
        """"""
    @overload
    def __init__(self, renewalTime: TimeSpan) -> None:
        """"""
    @property
    def RenewalTime(self) -> TimeSpan:
        """"""
    @RenewalTime.setter
    def RenewalTime(self, value: TimeSpan) -> None: ...
    def Close(self) -> None:
        """"""
    def CreateObjRef(self, requestedType: Type) -> ObjRef:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetLifetimeService(self) -> object:
        """"""
    def GetType(self) -> Type:
        """"""
    def InitializeLifetimeService(self) -> object:
        """"""
    def Register(self, obj: MarshalByRefObject) -> bool:
        """"""
    def Renewal(self, lease: ILease) -> TimeSpan:
        """"""
    def ToString(self) -> str:
        """"""
    def Unregister(self, obj: MarshalByRefObject) -> None:
        """"""

class ILease:
    """"""
    @property
    def CurrentLeaseTime(self) -> TimeSpan:
        """"""
    @property
    def CurrentState(self) -> LeaseState:
        """"""
    @property
    def InitialLeaseTime(self) -> TimeSpan:
        """"""
    @InitialLeaseTime.setter
    def InitialLeaseTime(self, value: TimeSpan) -> None: ...
    @property
    def RenewOnCallTime(self) -> TimeSpan:
        """"""
    @RenewOnCallTime.setter
    def RenewOnCallTime(self, value: TimeSpan) -> None: ...
    @property
    def SponsorshipTimeout(self) -> TimeSpan:
        """"""
    @SponsorshipTimeout.setter
    def SponsorshipTimeout(self, value: TimeSpan) -> None: ...
    @overload
    def Register(self, obj: ISponsor) -> None:
        """"""
    @overload
    def Register(self, obj: ISponsor, renewalTime: TimeSpan) -> None:
        """"""
    def Renew(self, renewalTime: TimeSpan) -> TimeSpan:
        """"""
    def Unregister(self, obj: ISponsor) -> None:
        """"""

class ISponsor:
    """"""
    def Renewal(self, lease: ILease) -> TimeSpan:
        """"""

class Lease(MarshalByRefObject, ILease):
    """"""
    @property
    def CurrentLeaseTime(self) -> TimeSpan:
        """"""
    @property
    def CurrentState(self) -> LeaseState:
        """"""
    @property
    def InitialLeaseTime(self) -> TimeSpan:
        """"""
    @InitialLeaseTime.setter
    def InitialLeaseTime(self, value: TimeSpan) -> None: ...
    @property
    def RenewOnCallTime(self) -> TimeSpan:
        """"""
    @RenewOnCallTime.setter
    def RenewOnCallTime(self, value: TimeSpan) -> None: ...
    @property
    def SponsorshipTimeout(self) -> TimeSpan:
        """"""
    @SponsorshipTimeout.setter
    def SponsorshipTimeout(self, value: TimeSpan) -> None: ...
    def CreateObjRef(self, requestedType: Type) -> ObjRef:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetLifetimeService(self) -> object:
        """"""
    def GetType(self) -> Type:
        """"""
    def InitializeLifetimeService(self) -> object:
        """"""
    @overload
    def Register(self, obj: ISponsor) -> None:
        """"""
    @overload
    def Register(self, obj: ISponsor, renewalTime: TimeSpan) -> None:
        """"""
    def Renew(self, renewalTime: TimeSpan) -> TimeSpan:
        """"""
    def ToString(self) -> str:
        """"""
    def Unregister(self, sponsor: ISponsor) -> None:
        """"""

class LeaseLifeTimeServiceProperty(Object, IContextProperty, IContributeObjectSink):
    """"""
    def __init__(self) -> None:
        """"""
    @property
    def Name(self) -> str:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def Freeze(self, newContext: Context) -> None:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetObjectSink(self, obj: MarshalByRefObject, nextSink: IMessageSink) -> IMessageSink:
        """"""
    def GetType(self) -> Type:
        """"""
    def IsNewContextOK(self, newCtx: Context) -> bool:
        """"""
    def ToString(self) -> str:
        """"""

class LeaseManager(Object):
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class LeaseSink(Object, IMessageSink):
    """"""
    def __init__(self, lease: Lease, nextSink: IMessageSink) -> None:
        """"""
    @property
    def NextSink(self) -> IMessageSink:
        """"""
    def AsyncProcessMessage(self, msg: IMessage, replySink: IMessageSink) -> IMessageCtrl:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def SyncProcessMessage(self, msg: IMessage) -> IMessage:
        """"""
    def ToString(self) -> str:
        """"""

class LeaseState(Enum):
    """"""

    Null: LeaseState = ...
    """"""
    Initial: LeaseState = ...
    """"""
    Active: LeaseState = ...
    """"""
    Renewing: LeaseState = ...
    """"""
    Expired: LeaseState = ...
    """"""

class LifetimeServices(Object):
    """"""
    def __init__(self) -> None:
        """"""
    @classmethod
    @property
    def LeaseManagerPollTime(cls) -> TimeSpan:
        """"""
    @classmethod
    @LeaseManagerPollTime.setter
    def LeaseManagerPollTime(cls, value: TimeSpan) -> None: ...
    @classmethod
    @property
    def LeaseTime(cls) -> TimeSpan:
        """"""
    @classmethod
    @LeaseTime.setter
    def LeaseTime(cls, value: TimeSpan) -> None: ...
    @classmethod
    @property
    def RenewOnCallTime(cls) -> TimeSpan:
        """"""
    @classmethod
    @RenewOnCallTime.setter
    def RenewOnCallTime(cls, value: TimeSpan) -> None: ...
    @classmethod
    @property
    def SponsorshipTimeout(cls) -> TimeSpan:
        """"""
    @classmethod
    @SponsorshipTimeout.setter
    def SponsorshipTimeout(cls, value: TimeSpan) -> None: ...
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""
