__all__ = [
    'CommittableTransaction',
    'DependentTransaction',
    'Enlistment',
    'PreparingEnlistment',
    'SinglePhaseEnlistment',
    'SubordinateTransaction',
    'Transaction',
    'TransactionAbortedException',
    'TransactionEventArgs',
    'TransactionException',
    'TransactionInDoubtException',
    'TransactionInformation',
    'TransactionInterop',
    'TransactionManager',
    'TransactionManagerCommunicationException',
    'TransactionPromotionException',
    'TransactionScope',
    'TransactionOptions',
    'IDtcTransaction',
    'IEnlistmentNotification',
    'IPromotableSinglePhaseNotification',
    'ISimpleTransactionSuperior',
    'ISinglePhaseNotification',
    'ITransactionPromoter',
    'DependentCloneOption',
    'EnlistmentOptions',
    'EnterpriseServicesInteropOption',
    'IsolationLevel',
    'TransactionScopeAsyncFlowOption',
    'TransactionScopeOption',
    'TransactionStatus',
    'HostCurrentTransactionCallback',
    'TransactionCompletedEventHandler',
    'TransactionStartedEventHandler',
]
# TODO

# ---------- CLASSES ---------- #

class CommittableTransaction:
    """Describes a committable transaction."""

class DependentTransaction:
    """Describes a clone of a transaction providing guarantee that the transaction cannot be committed until the application comes to rest regarding work on the transaction. This class cannot be inherited."""

class Enlistment:
    """Facilitates communication between an enlisted transaction participant and the transaction manager during the final phase of the transaction."""

class PreparingEnlistment:
    """Facilitates communication between an enlisted transaction participant and the transaction manager during the Prepare phase of the transaction."""

class SinglePhaseEnlistment:
    """Provides a set of callbacks that facilitate communication between a participant enlisted for Single Phase Commit and the transaction manager when the SinglePhaseCommit(SinglePhaseEnlistment) notification is received."""

class SubordinateTransaction:
    """Represents a non-rooted transaction that can be delegated. This class cannot be inherited."""

class Transaction:
    """Represents a transaction."""

class TransactionAbortedException:
    """The exception that is thrown when an operation is attempted on a transaction that has already been rolled back, or an attempt is made to commit the transaction and the transaction aborts."""

class TransactionEventArgs:
    """Provides data for the following transaction events: DistributedTransactionStarted, TransactionCompleted."""

class TransactionException:
    """The exception that is thrown when you attempt to do work on a transaction that cannot accept new work."""

class TransactionInDoubtException:
    """The exception that is thrown when an operation is attempted on a transaction that is in doubt, or an attempt is made to commit the transaction and the transaction becomes InDoubt."""

class TransactionInformation:
    """Provides additional information regarding a transaction."""

class TransactionInterop:
    """Facilitates interaction between System.Transactions and components that were previously written to interact with MSDTC, COM+, or System.EnterpriseServices. This class cannot be inherited."""

class TransactionManager:
    """Contains methods used for transaction management. This class cannot be inherited."""

class TransactionManagerCommunicationException:
    """The exception that is thrown when a resource manager cannot communicate with the transaction manager."""

class TransactionPromotionException:
    """The exception that is thrown when a promotion fails."""

class TransactionScope:
    """Makes a code block transactional. This class cannot be inherited."""


# ---------- STRUCTS ---------- #

class TransactionOptions:
    """Contains additional information that specifies transaction behaviors."""


# ---------- INTERFACES ---------- #

class IDtcTransaction:
    """Describes a DTC transaction."""

class IEnlistmentNotification:
    """Describes an interface that a resource manager should implement to provide two phase commit notification callbacks for the transaction manager upon enlisting for participation."""

class IPromotableSinglePhaseNotification:
    """Describes an object that acts as a commit delegate for a non-distributed transaction internal to a resource manager."""

class ISimpleTransactionSuperior:
    """Represents a transaction that is not a root transaction, but can be escalated to be managed by the MSDTC."""

class ISinglePhaseNotification:
    """Describes a resource object that supports single phase commit optimization to participate in a transaction."""

class ITransactionPromoter:
    """Describes a delegated transaction for an existing transaction that can be escalated to be managed by the MSDTC when needed."""


# ---------- ENUMS ---------- #

class DependentCloneOption:
    """Controls what kind of dependent transaction to create."""

class EnlistmentOptions:
    """Determines whether the object should be enlisted during the prepare phase."""

class EnterpriseServicesInteropOption:
    """Specifies how distributed transactions interact with COM+ transactions."""

class IsolationLevel:
    """Specifies the isolation level of a transaction."""

class TransactionScopeAsyncFlowOption:
    """Specifies whether transaction flow across thread continuations is enabled for TransactionScope."""

class TransactionScopeOption:
    """Provides additional options for creating a transaction scope."""

class TransactionStatus:
    """Describes the current status of a distributed transaction."""


# ---------- DELEGATES ---------- #

class HostCurrentTransactionCallback:
    """Provides a mechanism for the hosting environment to supply its own default notion of Current."""

class TransactionCompletedEventHandler:
    """Represents the method that handles the TransactionCompleted event of a Transaction class."""

class TransactionStartedEventHandler:
    """Represents the method that will handle the DistributedTransactionStarted event of a TransactionManager class."""
