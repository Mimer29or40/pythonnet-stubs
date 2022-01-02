__all__ = [
    'Activity',
    'ActivityListener',
    'ActivitySource',
    'ActivityTagsCollection',
    'BooleanSwitch',
    'ConditionalAttribute',
    'ConsoleTraceListener',
    'CorrelationManager',
    'DataReceivedEventArgs',
    'Debug',
    'DebuggableAttribute',
    'Debugger',
    'DebuggerBrowsableAttribute',
    'DebuggerDisplayAttribute',
    'DebuggerHiddenAttribute',
    'DebuggerNonUserCodeAttribute',
    'DebuggerStepperBoundaryAttribute',
    'DebuggerStepThroughAttribute',
    'DebuggerTypeProxyAttribute',
    'DebuggerVisualizerAttribute',
    'DefaultTraceListener',
    'DelimitedListTraceListener',
    'DiagnosticListener',
    'DiagnosticSource',
    'DistributedContextPropagator',
    'EventTypeFilter',
    'FileVersionInfo',
    'MonitoringDescriptionAttribute',
    'Process',
    'ProcessModule',
    'ProcessModuleCollection',
    'ProcessStartInfo',
    'ProcessThread',
    'ProcessThreadCollection',
    'SourceFilter',
    'SourceSwitch',
    'StackFrame',
    'StackFrameExtensions',
    'StackTrace',
    'StackTraceHiddenAttribute',
    'Stopwatch',
    'Switch',
    'SwitchAttribute',
    'SwitchLevelAttribute',
    'TextWriterTraceListener',
    'Trace',
    'TraceEventCache',
    'TraceFilter',
    'TraceListener',
    'TraceListenerCollection',
    'TraceSource',
    'TraceSwitch',
    'XmlWriterTraceListener',
    'ActivityContext',
    'ActivityCreationOptions',
    'ActivityEvent',
    'ActivityLink',
    'ActivitySpanId',
    'ActivityTagsCollection',
    'ActivityTraceId',
    'Debug',
    'Debug',
    'TagList',
    'TagList',
    'ActivityIdFormat',
    'ActivityKind',
    'ActivitySamplingResult',
    'ActivityStatusCode',
    'ActivityTraceFlags',
    'DebuggableAttribute',
    'DebuggerBrowsableState',
    'ProcessPriorityClass',
    'ProcessWindowStyle',
    'SourceLevels',
    'ThreadPriorityLevel',
    'ThreadState',
    'ThreadWaitReason',
    'TraceEventType',
    'TraceLevel',
    'TraceOptions',
    'DataReceivedEventHandler',
    'DistributedContextPropagator',
    'DistributedContextPropagator',
    'SampleActivity',
]

from typing import TypeVar, Generic

T = TypeVar('T')


# TODO

# ---------- CLASSES ---------- #

class Activity:
    """Represents an operation with context to be used for logging."""


class ActivityListener:
    """Allows listening to the start and stop activity events and gives the opportunity to decide creating an activity for sampling scenarios."""


class ActivitySource:
    """Provides APIs to create and start Activity objects and to register ActivityListener objects to listen to the Activity events."""


class ActivityTagsCollection:
    """ActivityTagsCollection is a collection class used to store tracing tags.
    
    This collection will be used with classes like ActivityEvent and ActivityLink.
    
    This collection behaves as follows:
    
    The collection items will be ordered according to how they are added.
    Don't allow duplication of items with the same key.
    When using the indexer to store an item in the collection:
    If the item has a key that previously existed in the collection and the value is null, the collection item matching the key will be removed from the collection.
    If the item has a key that previously existed in the collection and the value is not null, the new item value will replace the old value stored in the collection.
    Otherwise, the item will be added to the collection.
    Add method will add a new item to the collection if an item doesn't already exist with the same key. Otherwise, it will throw an exception.
    """
    
    # ---------- STRUCTS ---------- #
    
    class Enumerator:
        """Enumerates the elements of an ActivityTagsCollection."""


class BooleanSwitch:
    """Provides a simple on/off switch that controls debugging and tracing output."""


class ConditionalAttribute:
    """Indicates to compilers that a method call or attribute should be ignored unless a specified conditional compilation symbol is defined."""


class ConsoleTraceListener:
    """Directs tracing or debugging output to either the standard output or the standard error stream."""


class CorrelationManager:
    """Correlates traces that are part of a logical transaction."""


class DataReceivedEventArgs:
    """Provides data for the OutputDataReceived and ErrorDataReceived events."""


class Debug:
    """Provides a set of methods and properties that help debug your code."""
    
    # ---------- STRUCTS ---------- #
    
    class AssertInterpolatedStringHandler:
        """Provides an interpolated string handler for Assert(Boolean) that only performs formatting if the assert fails."""
    
    class WriteIfInterpolatedStringHandler:
        """Provides an interpolated string handler for WriteIf(Boolean, String) and WriteLineIf(Boolean, Object) that only performs formatting if the condition applies."""


class DebuggableAttribute:
    """Modifies code generation for runtime just-in-time (JIT) debugging. This class cannot be inherited."""
    
    # ---------- ENUMS ---------- #
    
    class DebuggingModes:
        """Specifies the debugging mode for the just-in-time (JIT) compiler."""


class Debugger:
    """Enables communication with a debugger. This class cannot be inherited."""


class DebuggerBrowsableAttribute:
    """Determines if and how a member is displayed in the debugger variable windows. This class cannot be inherited."""


class DebuggerDisplayAttribute:
    """Determines how a class or field is displayed in the debugger variable windows."""


class DebuggerHiddenAttribute:
    """Specifies the DebuggerHiddenAttribute. This class cannot be inherited."""


class DebuggerNonUserCodeAttribute:
    """Identifies a type or member that is not part of the user code for an application."""


class DebuggerStepperBoundaryAttribute:
    """Indicates the code following the attribute is to be executed in run, not step, mode."""


class DebuggerStepThroughAttribute:
    """Instructs the debugger to step through the code instead of stepping into the code. This class cannot be inherited."""


class DebuggerTypeProxyAttribute:
    """Specifies the display proxy for a type."""


class DebuggerVisualizerAttribute:
    """Specifies that the type has a visualizer. This class cannot be inherited."""


class DefaultTraceListener:
    """Provides the default output methods and behavior for tracing."""


class DelimitedListTraceListener:
    """Directs tracing or debugging output to a text writer, such as a stream writer, or to a stream, such as a file stream."""


class DiagnosticListener:
    """Provides an implementation of the abstract DiagnosticSource class that represents a named place to which a source sends its information (events)."""


class DiagnosticSource:
    """An abstract class that allows code to be instrumented for production-time logging of rich data payloads for consumption within the process that was instrumented."""


class DistributedContextPropagator:
    """An implementation of DistributedContextPropagator determines if and how distributed context information is encoded and decoded as it traverses the network. The encoding can be transported over any network protocol that supports string key-value pairs. For example, when using HTTP, each key-value pair is an HTTP header. DistributedContextPropagator injects values into and extracts values from carriers as string key-value pairs."""
    
    # ---------- DELEGATES ---------- #
    
    class PropagatorGetterCallback:
        """Represents the callback method that's used in the extract methods of propagators. The callback is invoked to look up the value of a named field."""
    
    class PropagatorSetterCallback:
        """Represents the callback method that's used in propagators' inject methods. This callback is invoked to set the value of a named field. Propagators may invoke it multiple times in order to set multiple fields."""


class EventTypeFilter:
    """Indicates whether a listener should trace based on the event type."""


class FileVersionInfo:
    """Provides version information for a physical file on disk."""


class MonitoringDescriptionAttribute:
    """Specifies a description for a property or event."""


class Process:
    """Provides access to local and remote processes and enables you to start and stop local system processes."""


class ProcessModule:
    """Represents a.dll or .exe file that is loaded into a particular process."""


class ProcessModuleCollection:
    """Provides a strongly typed collection of ProcessModule objects."""


class ProcessStartInfo:
    """Specifies a set of values that are used when you start a process."""


class ProcessThread:
    """Represents an operating system process thread."""


class ProcessThreadCollection:
    """Provides a strongly typed collection of ProcessThread objects."""


class SourceFilter:
    """Indicates whether a listener should trace a message based on the source of a trace."""


class SourceSwitch:
    """Provides a multilevel switch to control tracing and debug output without recompiling your code."""


class StackFrame:
    """Provides information about a StackFrame, which represents a function call on the call stack for the current thread."""


class StackFrameExtensions:
    """Provides extension methods for the StackFrame class, which represents a function call on the call stack for the current thread."""


class StackTrace:
    """Represents a stack trace, which is an ordered collection of one or more stack frames."""


class StackTraceHiddenAttribute:
    """Types and Methods attributed with StackTraceHidden will be omitted from the stack trace text shown in StackTrace.ToString() and Exception.StackTrace"""


class Stopwatch:
    """Provides a set of methods and properties that you can use to accurately measure elapsed time."""


class Switch:
    """Provides an abstract base class to create new debugging and tracing switches."""


class SwitchAttribute:
    """Identifies a switch used in an assembly, class, or member."""


class SwitchLevelAttribute:
    """Identifies the level type for a switch."""


class TextWriterTraceListener:
    """Directs tracing or debugging output to a TextWriter or to a Stream, such as FileStream."""


class Trace:
    """Provides a set of methods and properties that help you trace the execution of your code. This class cannot be inherited."""


class TraceEventCache:
    """Provides trace event data specific to a thread and a process."""


class TraceFilter:
    """Provides the base class for trace filter implementations."""


class TraceListener:
    """Provides the abstract base class for the listeners who monitor trace and debug output."""


class TraceListenerCollection:
    """Provides a thread-safe list of TraceListener objects."""


class TraceSource:
    """Provides a set of methods and properties that enable applications to trace the execution of code and associate trace messages with their source."""


class TraceSwitch:
    """Provides a multilevel switch to control tracing and debug output without recompiling your code."""


class XmlWriterTraceListener:
    """Directs tracing or debugging output as XML-encoded data to a TextWriter or to a Stream, such as a FileStream."""


# ---------- STRUCTS ---------- #

class ActivityContext:
    """A representation that conforms to the W3C TraceContext specification. It contains two identifiers: a TraceId and a SpanId, along with a set of common TraceFlags and system-specific TraceState values."""


class ActivityCreationOptions(Generic[T]):
    """Encapsulates all the information that is sent to the activity listener, to make decisions about the creation of the activity instance, as well as its state.
    
    The possible generic type parameters are ActivityContext or String.
    """


class ActivityEvent:
    """Represents an event containing a name and a timestamp, as well as an optional list of tags."""


class ActivityLink:
    """Activities may be linked to zero or more activity context instances that are causally related.
    
    Activity links can point to activity contexts inside a single trace or across different traces.
    
    Activity links can be used to represent batched operations where an activity was initiated by multiple initiating activities, each representing a single incoming item being processed in the batch.
    """


class ActivitySpanId:
    """Represents a SpanId formatted based on a W3C standard."""


class ActivityTraceId:
    """Represents a TraceId whose format is based on a W3C standard."""


class TagList:
    """Represents a list of tags that can be accessed by index. Provides methods to search, sort, and manipulate lists."""
    
    class Enumerator:
        """An enumerator for traversing a tag list collection."""


# ---------- ENUMS ---------- #

class ActivityIdFormat:
    """Specifies the format of the Id property."""


class ActivityKind:
    """Describes the relationship between the activity, its parents and its children in a trace."""


class ActivitySamplingResult:
    """Enumeration values used by ActivityListener to indicate the amount of data to collect for the related Activity. Requesting more data causes a greater performance overhead."""


class ActivityStatusCode:
    """Define the status code of the Activity which indicate the status of the instrumented operation."""


class ActivityTraceFlags:
    """Specifies flags defined by the W3C standard that are associated with an activity."""


class DebuggerBrowsableState:
    """Provides display instructions for the debugger."""


class ProcessPriorityClass:
    """Indicates the priority that the system associates with a process. This value, together with the priority value of each thread of the process, determines each thread's base priority level."""


class ProcessWindowStyle:
    """Specified how a new window should appear when the system starts a process."""


class SourceLevels:
    """Specifies the levels of trace messages filtered by the source switch and event type filter."""


class ThreadPriorityLevel:
    """Specifies the priority level of a thread."""


class ThreadState:
    """Specifies the current execution state of the thread."""


class ThreadWaitReason:
    """Specifies the reason a thread is waiting."""


class TraceEventType:
    """Identifies the type of event that has caused the trace."""


class TraceLevel:
    """Specifies what messages to output for the Debug, Trace and TraceSwitch classes."""


class TraceOptions:
    """Specifies trace data options to be written to the trace output."""


# ---------- DELEGATES ---------- #

class DataReceivedEventHandler:
    """Represents the method that will handle the OutputDataReceived event or ErrorDataReceived event of a Process."""


class SampleActivity(Generic[T]):
    """A delegate that defines the signature of the ActivityListener callbacks used in the sampling process."""
