__all__ = [
    'DiagnosticCounter',
    'EventAttribute',
    'EventCommandEventArgs',
    'EventCounter',
    'EventDataAttribute',
    'EventFieldAttribute',
    'EventIgnoreAttribute',
    'EventListener',
    'EventSource',
    'EventSourceAttribute',
    'EventSourceCreatedEventArgs',
    'EventSourceException',
    'EventWrittenEventArgs',
    'IncrementingEventCounter',
    'IncrementingPollingCounter',
    'NonEventAttribute',
    'PollingCounter',
    'EventSource',
    'EventSourceOptions',
    'EventActivityOptions',
    'EventChannel',
    'EventCommand',
    'EventFieldFormat',
    'EventFieldTags',
    'EventKeywords',
    'EventLevel',
    'EventManifestOptions',
    'EventOpcode',
    'EventSourceSettings',
    'EventTags',
    'EventTask',
]


# TODO

# ---------- CLASSES ---------- #

class DiagnosticCounter:
    """DiagnosticCounter is an abstract class that serves as the parent class for various Counter* classes, namely EventCounter, PollingCounter, IncrementingEventCounter, and IncrementingPollingCounter."""


class EventAttribute:
    """Specifies additional event schema information for an event."""


class EventCommandEventArgs:
    """Provides the arguments for the OnEventCommand(EventCommandEventArgs) callback."""


class EventCounter:
    """Provides the ability to collect statistics for very frequent events through the EventSource class."""


class EventDataAttribute:
    """Specifies a type to be passed to the Write<T>(String, EventSourceOptions, T) method."""


class EventFieldAttribute:
    """The EventFieldAttribute is placed on fields of user-defined types that are passed as EventSource payloads."""


class EventIgnoreAttribute:
    """Specifies a property should be ignored when writing an event type with the Write<T>(String, EventSourceOptions, T) method."""


class EventListener:
    """Provides methods for enabling and disabling events from event sources."""


class EventSource:
    """Provides the ability to create events for event tracing across platforms."""
    
    # ---------- STRUCTS ---------- #
    
    class EventData:
        """Provides the event data for creating fast WriteEvent overloads by using the WriteEventCore(Int32, Int32, EventSource+EventData*) method."""


class EventSourceAttribute:
    """Allows the event tracing for Windows (ETW) name to be defined independently of the name of the event source class."""


class EventSourceCreatedEventArgs:
    """Provides data for the EventSourceCreated event."""


class EventSourceException:
    """The exception that is thrown when an error occurs during event tracing for Windows (ETW)."""


class EventWrittenEventArgs:
    """Provides data for the OnEventWritten(EventWrittenEventArgs) callback."""


class IncrementingEventCounter:
    """Provides a variant of EventCounter for variables that are ever-increasing, such as the number of exceptions in the runtime."""


class IncrementingPollingCounter:
    """Provides a variant of EventCounter for variables that are ever-increasing, such as the number of exceptions in the runtime."""


class NonEventAttribute:
    """Identifies a method that is not generating an event."""


class PollingCounter:
    """Provides a variant of EventCounter that collects and calculates similar statistics as EventCounter."""


# ---------- STRUCTS ---------- #

class EventSourceOptions:
    """Specifies overrides of default event settings such as the log level, keywords and operation code when the Write<T>(String, EventSourceOptions, T) method is called."""


# ---------- ENUMS ---------- #

class EventActivityOptions:
    """Specifies the tracking of activity start and stop events."""


class EventChannel:
    """Specifies the event log channel for the event."""


class EventCommand:
    """Describes the command (Command property) that is passed to the OnEventCommand(EventCommandEventArgs) callback."""


class EventFieldFormat:
    """Specifies how to format the value of a user-defined type and can be used to override the default formatting for a field."""


class EventFieldTags:
    """Specifies the user-defined tag that is placed on fields of user-defined types that are passed as EventSource payloads through the EventFieldAttribute."""


class EventKeywords:
    """Defines the standard keywords that apply to events."""


class EventLevel:
    """Identifies the level of an event."""


class EventManifestOptions:
    """Specifies how the ETW manifest for the event source is generated."""


class EventOpcode:
    """Defines the standard operation codes that the event source attaches to events."""


class EventSourceSettings:
    """Specifies configuration options for an event source."""


class EventTags:
    """Specifies the tracking of activity start and stop events. You should only use the lower 24 bits. For more information, see EventSourceOptions and Write(String, EventSourceOptions)."""


class EventTask:
    """Defines the tasks that apply to events."""
