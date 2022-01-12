from __future__ import annotations

from typing import Protocol, Union, overload

from System import Boolean, Enum, Int32, MarshalByRefObject, Object, String, TimeSpan, Void
from System.Runtime.Remoting.Contexts import Context, IContextProperty, IContributeObjectSink
from System.Runtime.Remoting.Messaging import IMessage, IMessageCtrl, IMessageSink

# ---------- Types ---------- #

BooleanType = Union[bool, Boolean]
IntType = Union[int, Int32]
ObjectType = Object
StringType = Union[str, String]
VoidType = Union[None, Void]


# ---------- Classes ---------- #

class ClientSponsor(MarshalByRefObject, ISponsor):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self): ...
    
    @overload
    def __init__(self, renewalTime: TimeSpan): ...
    
    # ---------- Properties ---------- #
    
    @property
    def RenewalTime(self) -> TimeSpan: ...
    
    @RenewalTime.setter
    def RenewalTime(self, value: TimeSpan) -> None: ...
    
    # ---------- Methods ---------- #
    
    def Close(self) -> VoidType: ...
    
    def InitializeLifetimeService(self) -> ObjectType: ...
    
    def Register(self, obj: MarshalByRefObject) -> BooleanType: ...
    
    def Renewal(self, lease: ILease) -> TimeSpan: ...
    
    def Unregister(self, obj: MarshalByRefObject) -> VoidType: ...
    
    def get_RenewalTime(self) -> TimeSpan: ...
    
    def set_RenewalTime(self, value: TimeSpan) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class Lease(MarshalByRefObject, ILease):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @property
    def CurrentLeaseTime(self) -> TimeSpan: ...
    
    @property
    def CurrentState(self) -> LeaseState: ...
    
    @property
    def InitialLeaseTime(self) -> TimeSpan: ...
    
    @InitialLeaseTime.setter
    def InitialLeaseTime(self, value: TimeSpan) -> None: ...
    
    @property
    def RenewOnCallTime(self) -> TimeSpan: ...
    
    @RenewOnCallTime.setter
    def RenewOnCallTime(self, value: TimeSpan) -> None: ...
    
    @property
    def SponsorshipTimeout(self) -> TimeSpan: ...
    
    @SponsorshipTimeout.setter
    def SponsorshipTimeout(self, value: TimeSpan) -> None: ...
    
    # ---------- Methods ---------- #
    
    def InitializeLifetimeService(self) -> ObjectType: ...
    
    @overload
    def Register(self, obj: ISponsor) -> VoidType: ...
    
    @overload
    def Register(self, obj: ISponsor, renewalTime: TimeSpan) -> VoidType: ...
    
    def Renew(self, renewalTime: TimeSpan) -> TimeSpan: ...
    
    def Unregister(self, sponsor: ISponsor) -> VoidType: ...
    
    def get_CurrentLeaseTime(self) -> TimeSpan: ...
    
    def get_CurrentState(self) -> LeaseState: ...
    
    def get_InitialLeaseTime(self) -> TimeSpan: ...
    
    def get_RenewOnCallTime(self) -> TimeSpan: ...
    
    def get_SponsorshipTimeout(self) -> TimeSpan: ...
    
    def set_InitialLeaseTime(self, value: TimeSpan) -> VoidType: ...
    
    def set_RenewOnCallTime(self, value: TimeSpan) -> VoidType: ...
    
    def set_SponsorshipTimeout(self, value: TimeSpan) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class LeaseLifeTimeServiceProperty(ObjectType, IContextProperty, IContributeObjectSink):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # ---------- Properties ---------- #
    
    @property
    def Name(self) -> StringType: ...
    
    # ---------- Methods ---------- #
    
    def Freeze(self, newContext: Context) -> VoidType: ...
    
    def GetObjectSink(self, obj: MarshalByRefObject, nextSink: IMessageSink) -> IMessageSink: ...
    
    def IsNewContextOK(self, newCtx: Context) -> BooleanType: ...
    
    def get_Name(self) -> StringType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class LeaseManager(ObjectType):
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


class LeaseSink(ObjectType, IMessageSink):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, lease: Lease, nextSink: IMessageSink): ...
    
    # ---------- Properties ---------- #
    
    @property
    def NextSink(self) -> IMessageSink: ...
    
    # ---------- Methods ---------- #
    
    def AsyncProcessMessage(self, msg: IMessage, replySink: IMessageSink) -> IMessageCtrl: ...
    
    def SyncProcessMessage(self, msg: IMessage) -> IMessage: ...
    
    def get_NextSink(self) -> IMessageSink: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class LifetimeServices(ObjectType):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # ---------- Properties ---------- #
    
    @staticmethod
    @property
    def LeaseManagerPollTime() -> TimeSpan: ...
    
    @staticmethod
    @LeaseManagerPollTime.setter
    def LeaseManagerPollTime(value: TimeSpan) -> None: ...
    
    @staticmethod
    @property
    def LeaseTime() -> TimeSpan: ...
    
    @staticmethod
    @LeaseTime.setter
    def LeaseTime(value: TimeSpan) -> None: ...
    
    @staticmethod
    @property
    def RenewOnCallTime() -> TimeSpan: ...
    
    @staticmethod
    @RenewOnCallTime.setter
    def RenewOnCallTime(value: TimeSpan) -> None: ...
    
    @staticmethod
    @property
    def SponsorshipTimeout() -> TimeSpan: ...
    
    @staticmethod
    @SponsorshipTimeout.setter
    def SponsorshipTimeout(value: TimeSpan) -> None: ...
    
    # ---------- Methods ---------- #
    
    @staticmethod
    def get_LeaseManagerPollTime() -> TimeSpan: ...
    
    @staticmethod
    def get_LeaseTime() -> TimeSpan: ...
    
    @staticmethod
    def get_RenewOnCallTime() -> TimeSpan: ...
    
    @staticmethod
    def get_SponsorshipTimeout() -> TimeSpan: ...
    
    @staticmethod
    def set_LeaseManagerPollTime(value: TimeSpan) -> VoidType: ...
    
    @staticmethod
    def set_LeaseTime(value: TimeSpan) -> VoidType: ...
    
    @staticmethod
    def set_RenewOnCallTime(value: TimeSpan) -> VoidType: ...
    
    @staticmethod
    def set_SponsorshipTimeout(value: TimeSpan) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


# No Structs

# ---------- Interfaces ---------- #

class ILease(Protocol):
    # ---------- Properties ---------- #
    
    @property
    def CurrentLeaseTime(self) -> TimeSpan: ...
    
    @property
    def CurrentState(self) -> LeaseState: ...
    
    @property
    def InitialLeaseTime(self) -> TimeSpan: ...
    
    @InitialLeaseTime.setter
    def InitialLeaseTime(self, value: TimeSpan) -> None: ...
    
    @property
    def RenewOnCallTime(self) -> TimeSpan: ...
    
    @RenewOnCallTime.setter
    def RenewOnCallTime(self, value: TimeSpan) -> None: ...
    
    @property
    def SponsorshipTimeout(self) -> TimeSpan: ...
    
    @SponsorshipTimeout.setter
    def SponsorshipTimeout(self, value: TimeSpan) -> None: ...
    
    # ---------- Methods ---------- #
    
    @overload
    def Register(self, obj: ISponsor, renewalTime: TimeSpan) -> VoidType: ...
    
    @overload
    def Register(self, obj: ISponsor) -> VoidType: ...
    
    def Renew(self, renewalTime: TimeSpan) -> TimeSpan: ...
    
    def Unregister(self, obj: ISponsor) -> VoidType: ...
    
    def get_CurrentLeaseTime(self) -> TimeSpan: ...
    
    def get_CurrentState(self) -> LeaseState: ...
    
    def get_InitialLeaseTime(self) -> TimeSpan: ...
    
    def get_RenewOnCallTime(self) -> TimeSpan: ...
    
    def get_SponsorshipTimeout(self) -> TimeSpan: ...
    
    def set_InitialLeaseTime(self, value: TimeSpan) -> VoidType: ...
    
    def set_RenewOnCallTime(self, value: TimeSpan) -> VoidType: ...
    
    def set_SponsorshipTimeout(self, value: TimeSpan) -> VoidType: ...
    
    # No Events


class ISponsor(Protocol):
    # No Properties
    
    # ---------- Methods ---------- #
    
    def Renewal(self, lease: ILease) -> TimeSpan: ...
    
    # No Events


# ---------- Enums ---------- #

class LeaseState(Enum):
    Null = 0
    Initial = 1
    Active = 2
    Renewing = 3
    Expired = 4


# No Delegates

__all__ = [
    ClientSponsor,
    Lease,
    LeaseLifeTimeServiceProperty,
    LeaseManager,
    LeaseSink,
    LifetimeServices,
    ILease,
    ISponsor,
    LeaseState,
]
