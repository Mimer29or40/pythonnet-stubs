from __future__ import annotations

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
    def __init__(self):
        """"""
    @overload
    def __init__(self, renewalTime: TimeSpan):
        """

        :param renewalTime:
        """
    @property
    def RenewalTime(self) -> TimeSpan:
        """

        :return:
        """
    @RenewalTime.setter
    def RenewalTime(self, value: TimeSpan) -> None: ...
    def Close(self) -> None:
        """"""
    def CreateObjRef(self, requestedType: Type) -> ObjRef:
        """

        :param requestedType:
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
    def Register(self, obj: MarshalByRefObject) -> bool:
        """

        :param obj:
        :return:
        """
    def Renewal(self, lease: ILease) -> TimeSpan:
        """

        :param lease:
        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """
    def Unregister(self, obj: MarshalByRefObject) -> None:
        """

        :param obj:
        """

class ILease:
    """"""

    @property
    def CurrentLeaseTime(self) -> TimeSpan:
        """

        :return:
        """
    @property
    def CurrentState(self) -> LeaseState:
        """

        :return:
        """
    @property
    def InitialLeaseTime(self) -> TimeSpan:
        """

        :return:
        """
    @InitialLeaseTime.setter
    def InitialLeaseTime(self, value: TimeSpan) -> None: ...
    @property
    def RenewOnCallTime(self) -> TimeSpan:
        """

        :return:
        """
    @RenewOnCallTime.setter
    def RenewOnCallTime(self, value: TimeSpan) -> None: ...
    @property
    def SponsorshipTimeout(self) -> TimeSpan:
        """

        :return:
        """
    @SponsorshipTimeout.setter
    def SponsorshipTimeout(self, value: TimeSpan) -> None: ...
    @overload
    def Register(self, obj: ISponsor) -> None:
        """

        :param obj:
        """
    @overload
    def Register(self, obj: ISponsor, renewalTime: TimeSpan) -> None:
        """

        :param obj:
        :param renewalTime:
        """
    def Renew(self, renewalTime: TimeSpan) -> TimeSpan:
        """

        :param renewalTime:
        :return:
        """
    def Unregister(self, obj: ISponsor) -> None:
        """

        :param obj:
        """

class ISponsor:
    """"""

    def Renewal(self, lease: ILease) -> TimeSpan:
        """

        :param lease:
        :return:
        """

class Lease(MarshalByRefObject, ILease):
    """"""

    @property
    def CurrentLeaseTime(self) -> TimeSpan:
        """

        :return:
        """
    @property
    def CurrentState(self) -> LeaseState:
        """

        :return:
        """
    @property
    def InitialLeaseTime(self) -> TimeSpan:
        """

        :return:
        """
    @InitialLeaseTime.setter
    def InitialLeaseTime(self, value: TimeSpan) -> None: ...
    @property
    def RenewOnCallTime(self) -> TimeSpan:
        """

        :return:
        """
    @RenewOnCallTime.setter
    def RenewOnCallTime(self, value: TimeSpan) -> None: ...
    @property
    def SponsorshipTimeout(self) -> TimeSpan:
        """

        :return:
        """
    @SponsorshipTimeout.setter
    def SponsorshipTimeout(self, value: TimeSpan) -> None: ...
    def CreateObjRef(self, requestedType: Type) -> ObjRef:
        """

        :param requestedType:
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
    @overload
    def Register(self, obj: ISponsor) -> None:
        """

        :param obj:
        """
    @overload
    def Register(self, obj: ISponsor, renewalTime: TimeSpan) -> None:
        """

        :param obj:
        :param renewalTime:
        """
    def Renew(self, renewalTime: TimeSpan) -> TimeSpan:
        """

        :param renewalTime:
        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """
    def Unregister(self, obj: ISponsor) -> None:
        """

        :param obj:
        """

class LeaseLifeTimeServiceProperty(Object, IContextProperty, IContributeObjectSink):
    """"""

    def __init__(self):
        """"""
    @property
    def Name(self) -> str:
        """

        :return:
        """
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def Freeze(self, newContext: Context) -> None:
        """

        :param newContext:
        """
    def GetHashCode(self) -> int:
        """

        :return:
        """
    def GetObjectSink(self, obj: MarshalByRefObject, nextSink: IMessageSink) -> IMessageSink:
        """

        :param obj:
        :param nextSink:
        :return:
        """
    def GetType(self) -> Type:
        """

        :return:
        """
    def IsNewContextOK(self, newCtx: Context) -> bool:
        """

        :param newCtx:
        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """

class LeaseManager(Object):
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

class LeaseSink(Object, IMessageSink):
    """"""

    def __init__(self, lease: Lease, nextSink: IMessageSink):
        """

        :param lease:
        :param nextSink:
        """
    @property
    def NextSink(self) -> IMessageSink:
        """

        :return:
        """
    def AsyncProcessMessage(self, msg: IMessage, replySink: IMessageSink) -> IMessageCtrl:
        """

        :param msg:
        :param replySink:
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
    def SyncProcessMessage(self, msg: IMessage) -> IMessage:
        """

        :param msg:
        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """

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

    def __init__(self):
        """"""
    @classmethod
    @property
    def LeaseManagerPollTime(cls) -> TimeSpan:
        """

        :return:
        """
    @classmethod
    @LeaseManagerPollTime.setter
    def LeaseManagerPollTime(cls, value: TimeSpan) -> None: ...
    @classmethod
    @property
    def LeaseTime(cls) -> TimeSpan:
        """

        :return:
        """
    @classmethod
    @LeaseTime.setter
    def LeaseTime(cls, value: TimeSpan) -> None: ...
    @classmethod
    @property
    def RenewOnCallTime(cls) -> TimeSpan:
        """

        :return:
        """
    @classmethod
    @RenewOnCallTime.setter
    def RenewOnCallTime(cls, value: TimeSpan) -> None: ...
    @classmethod
    @property
    def SponsorshipTimeout(cls) -> TimeSpan:
        """

        :return:
        """
    @classmethod
    @SponsorshipTimeout.setter
    def SponsorshipTimeout(cls, value: TimeSpan) -> None: ...
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
