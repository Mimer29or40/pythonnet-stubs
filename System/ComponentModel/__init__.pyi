__all__ = [
    'AddingNewEventArgs',
    'AmbientValueAttribute',
    'ArrayConverter',
    'AsyncCompletedEventArgs',
    'AsyncOperation',
    'AsyncOperationManager',
    'AttributeCollection',
    'AttributeProviderAttribute',
    'BackgroundWorker',
    'BaseNumberConverter',
    'BindableAttribute',
    'BindingList',
    'BooleanConverter',
    'BrowsableAttribute',
    'ByteConverter',
    'CancelEventArgs',
    'CategoryAttribute',
    'CharConverter',
    'CollectionChangeEventArgs',
    'CollectionConverter',
    'ComplexBindingPropertiesAttribute',
    'Component',
    'ComponentCollection',
    'ComponentConverter',
    'ComponentEditor',
    'ComponentResourceManager',
    'Container',
    'ContainerFilterService',
    'CultureInfoConverter',
    'CustomTypeDescriptor',
    'DataErrorsChangedEventArgs',
    'DataObjectAttribute',
    'DataObjectFieldAttribute',
    'DataObjectMethodAttribute',
    'DateTimeConverter',
    'DateTimeOffsetConverter',
    'DecimalConverter',
    'DefaultBindingPropertyAttribute',
    'DefaultEventAttribute',
    'DefaultPropertyAttribute',
    'DefaultValueAttribute',
    'DescriptionAttribute',
    'DesignerAttribute',
    'DesignerCategoryAttribute',
    'DesignerSerializationVisibilityAttribute',
    'DesignOnlyAttribute',
    'DesignTimeVisibleAttribute',
    'DisplayNameAttribute',
    'DoubleConverter',
    'DoWorkEventArgs',
    'EditorAttribute',
    'EditorBrowsableAttribute',
    'EnumConverter',
    'EventDescriptor',
    'EventDescriptorCollection',
    'EventHandlerList',
    'ExpandableObjectConverter',
    'ExtenderProvidedPropertyAttribute',
    'GuidConverter',
    'HandledEventArgs',
    'ImmutableObjectAttribute',
    'InheritanceAttribute',
    'InitializationEventAttribute',
    'InstallerTypeAttribute',
    'InstanceCreationEditor',
    'Int16Converter',
    'Int32Converter',
    'Int64Converter',
    'InvalidAsynchronousStateException',
    'InvalidEnumArgumentException',
    'License',
    'LicenseContext',
    'LicenseException',
    'LicenseManager',
    'LicenseProvider',
    'LicenseProviderAttribute',
    'LicFileLicenseProvider',
    'ListBindableAttribute',
    'ListChangedEventArgs',
    'ListSortDescription',
    'ListSortDescriptionCollection',
    'LocalizableAttribute',
    'LookupBindingPropertiesAttribute',
    'MarshalByValueComponent',
    'MaskedTextProvider',
    'MemberDescriptor',
    'MergablePropertyAttribute',
    'MultilineStringConverter',
    'NestedContainer',
    'NotifyParentPropertyAttribute',
    'NullableConverter',
    'ParenthesizePropertyNameAttribute',
    'PasswordPropertyTextAttribute',
    'ProgressChangedEventArgs',
    'PropertyChangedEventArgs',
    'PropertyChangingEventArgs',
    'PropertyDescriptor',
    'PropertyDescriptorCollection',
    'PropertyTabAttribute',
    'ProvidePropertyAttribute',
    'ReadOnlyAttribute',
    'RecommendedAsConfigurableAttribute',
    'ReferenceConverter',
    'RefreshEventArgs',
    'RefreshPropertiesAttribute',
    'RunInstallerAttribute',
    'RunWorkerCompletedEventArgs',
    'SByteConverter',
    'SettingsBindableAttribute',
    'SingleConverter',
    'StringConverter',
    'SyntaxCheck',
    'TimeSpanConverter',
    'ToolboxItemAttribute',
    'ToolboxItemFilterAttribute',
    'TypeConverter',
    'TypeConverter',
    'TypeConverter',
    'TypeConverterAttribute',
    'TypeDescriptionProvider',
    'TypeDescriptionProviderAttribute',
    'TypeDescriptor',
    'TypeListConverter',
    'UInt16Converter',
    'UInt32Converter',
    'UInt64Converter',
    'VersionConverter',
    'WarningException',
    'Win32Exception',
    'IBindingList',
    'IBindingListView',
    'ICancelAddNew',
    'IChangeTracking',
    'IComNativeDescriptorHandler',
    'IComponent',
    'IContainer',
    'ICustomTypeDescriptor',
    'IDataErrorInfo',
    'IEditableObject',
    'IExtenderProvider',
    'IIntellisenseBuilder',
    'IListSource',
    'INestedContainer',
    'INestedSite',
    'INotifyDataErrorInfo',
    'INotifyPropertyChanged',
    'INotifyPropertyChanging',
    'IRaiseItemChangedEvents',
    'IRevertibleChangeTracking',
    'ISite',
    'ISupportInitialize',
    'ISupportInitializeNotification',
    'ISynchronizeInvoke',
    'ITypeDescriptorContext',
    'ITypedList',
    'BindableSupport',
    'BindingDirection',
    'CollectionChangeAction',
    'DataObjectMethodType',
    'DesignerSerializationVisibility',
    'EditorBrowsableState',
    'InheritanceLevel',
    'LicenseUsageMode',
    'ListChangedType',
    'ListSortDirection',
    'MaskedTextResultHint',
    'PropertyTabScope',
    'RefreshProperties',
    'ToolboxItemFilterType',
    'AddingNewEventHandler',
    'AsyncCompletedEventHandler',
    'CancelEventHandler',
    'CollectionChangeEventHandler',
    'DoWorkEventHandler',
    'HandledEventHandler',
    'ListChangedEventHandler',
    'ProgressChangedEventHandler',
    'PropertyChangedEventHandler',
    'PropertyChangingEventHandler',
    'RefreshEventHandler',
    'RunWorkerCompletedEventHandler',
]

from typing import TypeVar, Generic

T = TypeVar('T')


# TODO

# ---------- CLASSES ---------- #

class AddingNewEventArgs:
    """Provides data for the AddingNew event."""


class AmbientValueAttribute:
    """Specifies the value to pass to a property to cause the property to get its value from another source. This is known as ambience. This class cannot be inherited."""


class ArrayConverter:
    """Provides a type converter to convert Array objects to and from various other representations."""


class AsyncCompletedEventArgs:
    """Provides data for the MethodNameCompleted event."""


class AsyncOperation:
    """Tracks the lifetime of an asynchronous operation."""


class AsyncOperationManager:
    """Provides concurrency management for classes that support asynchronous method calls. This class cannot be inherited."""


class AttributeCollection:
    """Represents a collection of attributes."""


class AttributeProviderAttribute:
    """Enables attribute redirection. This class cannot be inherited."""


class BackgroundWorker:
    """Executes an operation on a separate thread."""


class BaseNumberConverter:
    """Provides a base type converter for nonfloating-point numerical types."""


class BindableAttribute:
    """Specifies whether a member is typically used for binding. This class cannot be inherited."""


class BindingList(Generic[T]):
    """Provides a generic collection that supports data binding."""


class BooleanConverter:
    """Provides a type converter to convert Boolean objects to and from various other representations."""


class BrowsableAttribute:
    """Specifies whether a property or event should be displayed in a Properties window."""


class ByteConverter:
    """Provides a type converter to convert 8-bit unsigned integer objects to and from various other representations."""


class CancelEventArgs:
    """Provides data for a cancelable event."""


class CategoryAttribute:
    """Specifies the name of the category in which to group the property or event when displayed in a PropertyGrid control set to Categorized mode."""


class CharConverter:
    """Provides a type converter to convert Unicode character objects to and from various other representations."""


class CollectionChangeEventArgs:
    """Provides data for the CollectionChanged event."""


class CollectionConverter:
    """Provides a type converter to convert collection objects to and from various other representations."""


class ComplexBindingPropertiesAttribute:
    """Specifies the data source and data member properties for a component that supports complex data binding. This class cannot be inherited."""


class Component:
    """Provides the base implementation for the IComponent interface and enables object sharing between applications."""


class ComponentCollection:
    """Provides a read-only container for a collection of IComponent objects."""


class ComponentConverter:
    """Provides a type converter to convert components to and from various other representations."""


class ComponentEditor:
    """Provides the base class for a custom component editor."""


class ComponentResourceManager:
    """Provides simple functionality for enumerating resources for a component or object. The ComponentResourceManager class is a ResourceManager."""


class Container:
    """Encapsulates zero or more components."""


class ContainerFilterService:
    """Provides a base class for the container filter service."""


class CultureInfoConverter:
    """Provides a type converter to convert CultureInfo objects to and from various other representations."""


class CustomTypeDescriptor:
    """Provides a simple default implementation of the ICustomTypeDescriptor interface."""


class DataErrorsChangedEventArgs:
    """Provides data for the ErrorsChanged event."""


class DataObjectAttribute:
    """Identifies a type as an object suitable for binding to an ObjectDataSource object. This class cannot be inherited."""


class DataObjectFieldAttribute:
    """Provides metadata for a property representing a data field. This class cannot be inherited."""


class DataObjectMethodAttribute:
    """Identifies a data operation method exposed by a type, what type of operation the method performs, and whether the method is the default data method. This class cannot be inherited."""


class DateTimeConverter:
    """Provides a type converter to convert DateTime objects to and from various other representations."""


class DateTimeOffsetConverter:
    """Provides a type converter to convert DateTimeOffset structures to and from various other representations."""


class DecimalConverter:
    """Provides a type converter to convert Decimal objects to and from various other representations."""


class DefaultBindingPropertyAttribute:
    """Specifies the default binding property for a component. This class cannot be inherited."""


class DefaultEventAttribute:
    """Specifies the default event for a component."""


class DefaultPropertyAttribute:
    """Specifies the default property for a component."""


class DefaultValueAttribute:
    """Specifies the default value for a property."""


class DescriptionAttribute:
    """Specifies a description for a property or event."""


class DesignerAttribute:
    """Specifies the class used to implement design-time services for a component."""


class DesignerCategoryAttribute:
    """Specifies that the designer for a class belongs to a certain category."""


class DesignerSerializationVisibilityAttribute:
    """Specifies the type of persistence to use when serializing a property on a component at design time."""


class DesignOnlyAttribute:
    """Specifies whether a property can only be set at design time."""


class DesignTimeVisibleAttribute:
    """DesignTimeVisibleAttribute marks a component's visibility. If Yes is present, a visual designer can show this component on a designer."""


class DisplayNameAttribute:
    """Specifies the display name for a property, event, or public void method which takes no arguments."""


class DoubleConverter:
    """Provides a type converter to convert double-precision, floating point number objects to and from various other representations."""


class DoWorkEventArgs:
    """Provides data for the DoWork event handler."""


class EditorAttribute:
    """Specifies the editor to use to change a property. This class cannot be inherited."""


class EditorBrowsableAttribute:
    """Specifies that a property or method is viewable in an editor. This class cannot be inherited."""


class EnumConverter:
    """Provides a type converter to convert Enum objects to and from various other representations."""


class EventDescriptor:
    """Provides information about an event."""


class EventDescriptorCollection:
    """Represents a collection of EventDescriptor objects."""


class EventHandlerList:
    """Provides a simple list of delegates. This class cannot be inherited."""


class ExpandableObjectConverter:
    """Provides a type converter to convert expandable objects to and from various other representations."""


class ExtenderProvidedPropertyAttribute:
    """Specifies a property that is offered by an extender provider. This class cannot be inherited."""


class GuidConverter:
    """Provides a type converter to convert Guid objects to and from various other representations."""


class HandledEventArgs:
    """Provides data for events that can be handled completely in an event handler."""


class ImmutableObjectAttribute:
    """Specifies that an object has no subproperties capable of being edited. This class cannot be inherited."""


class InheritanceAttribute:
    """Indicates whether the component associated with this attribute has been inherited from a base class. This class cannot be inherited."""


class InitializationEventAttribute:
    """Specifies which event is raised on initialization. This class cannot be inherited."""


class InstallerTypeAttribute:
    """Specifies the installer for a type that installs components."""


class InstanceCreationEditor:
    """Creates an instance of a particular type of property from a drop-down box within the PropertyGrid."""


class Int16Converter:
    """Provides a type converter to convert 16-bit signed integer objects to and from other representations."""


class Int32Converter:
    """Provides a type converter to convert 32-bit signed integer objects to and from other representations."""


class Int64Converter:
    """Provides a type converter to convert 64-bit signed integer objects to and from various other representations."""


class InvalidAsynchronousStateException:
    """Thrown when a thread on which an operation should execute no longer exists or has no message loop."""


class InvalidEnumArgumentException:
    """The exception thrown when using invalid arguments that are enumerators."""


class License:
    """Provides the abstract base class for all licenses. A license is granted to a specific instance of a component."""


class LicenseContext:
    """Specifies when you can use a licensed object and provides a way of obtaining additional services needed to support licenses running within its domain."""


class LicenseException:
    """Represents the exception thrown when a component cannot be granted a license."""


class LicenseManager:
    """Provides properties and methods to add a license to a component and to manage a LicenseProvider. This class cannot be inherited."""


class LicenseProvider:
    """Provides the abstract base class for implementing a license provider."""


class LicenseProviderAttribute:
    """Specifies the LicenseProvider to use with a class. This class cannot be inherited."""


class LicFileLicenseProvider:
    """Provides an implementation of a LicenseProvider. The provider works in a similar fashion to the Microsoft .NET Framework standard licensing model."""


class ListBindableAttribute:
    """Specifies that a list can be used as a data source. A visual designer should use this attribute to determine whether to display a particular list in a data-binding picker. This class cannot be inherited."""


class ListChangedEventArgs:
    """Provides data for the ListChanged event."""


class ListSortDescription:
    """Provides a description of the sort operation applied to a data source."""


class ListSortDescriptionCollection:
    """Represents a collection of ListSortDescription objects."""


class LocalizableAttribute:
    """Specifies whether a property or parameter should be localized. This class cannot be inherited."""


class LookupBindingPropertiesAttribute:
    """Specifies the properties that support lookup-based binding. This class cannot be inherited."""


class MarshalByValueComponent:
    """Implements IComponent and provides the base implementation for remotable components that are marshaled by value (a copy of the serialized object is passed)."""


class MaskedTextProvider:
    """Represents a mask-parsing service that can be used by any number of controls that support masking, such as the MaskedTextBox control."""


class MemberDescriptor:
    """Represents a class member, such as a property or event. This is an abstract base class."""


class MergablePropertyAttribute:
    """Specifies that this property can be combined with properties belonging to other objects in a Properties window."""


class MultilineStringConverter:
    """Provides a type converter to convert multiline strings to a simple string."""


class NestedContainer:
    """Provides the base implementation for the INestedContainer interface, which enables containers to have an owning component."""


class NotifyParentPropertyAttribute:
    """Indicates that the parent property is notified when the value of the property that this attribute is applied to is modified. This class cannot be inherited."""


class NullableConverter:
    """Provides automatic conversion between a nullable type and its underlying primitive type."""


class ParenthesizePropertyNameAttribute:
    """Indicates whether the name of the associated property is displayed with parentheses in the Properties window. This class cannot be inherited."""


class PasswordPropertyTextAttribute:
    """Indicates that an object's text representation is obscured by characters such as asterisks. This class cannot be inherited."""


class ProgressChangedEventArgs:
    """Provides data for the ProgressChanged event."""


class PropertyChangedEventArgs:
    """Provides data for the PropertyChanged event."""


class PropertyChangingEventArgs:
    """Provides data for the PropertyChanging event."""


class PropertyDescriptor:
    """Provides an abstraction of a property on a class."""


class PropertyDescriptorCollection:
    """Represents a collection of PropertyDescriptor objects."""


class PropertyTabAttribute:
    """Identifies the property tab or tabs to display for the specified class or classes."""


class ProvidePropertyAttribute:
    """Specifies the name of the property that an implementer of IExtenderProvider offers to other components. This class cannot be inherited."""


class ReadOnlyAttribute:
    """Specifies whether the property this attribute is bound to is read-only or read/write. This class cannot be inherited."""


class RecommendedAsConfigurableAttribute:
    """Specifies that the property can be used as an application setting."""


class ReferenceConverter:
    """Provides a type converter to convert object references to and from other representations."""


class RefreshEventArgs:
    """Provides data for the Refreshed event."""


class RefreshPropertiesAttribute:
    """Indicates that the property grid should refresh when the associated property value changes. This class cannot be inherited."""


class RunInstallerAttribute:
    """Specifies whether the Visual Studio Custom Action Installer or the Installutil.exe (Installer Tool) should be invoked when the assembly is installed."""


class RunWorkerCompletedEventArgs:
    """Provides data for the MethodNameCompleted event."""


class SByteConverter:
    """Provides a type converter to convert 8-bit unsigned integer objects to and from a string."""


class SettingsBindableAttribute:
    """Specifies when a component property can be bound to an application setting."""


class SingleConverter:
    """Provides a type converter to convert single-precision, floating point number objects to and from various other representations."""


class StringConverter:
    """Provides a type converter to convert string objects to and from other representations."""


class SyntaxCheck:
    """Provides methods to verify the machine name and path conform to a specific syntax. This class cannot be inherited."""


class TimeSpanConverter:
    """Provides a type converter to convert TimeSpan objects to and from other representations."""


class ToolboxItemAttribute:
    """Represents an attribute of a toolbox item."""


class ToolboxItemFilterAttribute:
    """Specifies the filter string and filter type to use for a toolbox item."""


class TypeConverter:
    """Provides a unified way of converting types of values to other types, as well as for accessing standard values and subproperties."""
    
    class SimplePropertyDescriptor:
        """Represents an abstract class that provides properties for objects that do not have properties."""
    
    class StandardValuesCollection:
        """Represents a collection of values."""


class TypeConverterAttribute:
    """Specifies what type to use as a converter for the object this attribute is bound to."""


class TypeDescriptionProvider:
    """Provides supplemental metadata to the TypeDescriptor."""


class TypeDescriptionProviderAttribute:
    """Specifies the custom type description provider for a class. This class cannot be inherited."""


class TypeDescriptor:
    """Provides information about the characteristics for a component, such as its attributes, properties, and events. This class cannot be inherited."""


class TypeListConverter:
    """Provides a type converter that can be used to populate a list box with available types."""


class UInt16Converter:
    """Provides a type converter to convert 16-bit unsigned integer objects to and from other representations."""


class UInt32Converter:
    """Provides a type converter to convert 32-bit unsigned integer objects to and from various other representations."""


class UInt64Converter:
    """Provides a type converter to convert 64-bit unsigned integer objects to and from other representations."""


class VersionConverter:
    """Provides a type converter to convert Version objects to and from various other representations."""


class WarningException:
    """Specifies an exception that is handled as a warning instead of an error."""


class Win32Exception:
    """Throws an exception for a Win32 error code."""


# ---------- INTERFACES ---------- #

class IBindingList:
    """Provides the features required to support both complex and simple scenarios when binding to a data source."""


class IBindingListView:
    """Extends the IBindingList interface by providing advanced sorting and filtering capabilities."""


class ICancelAddNew:
    """Adds transactional capability when adding a new item to a collection."""


class IChangeTracking:
    """Defines the mechanism for querying the object for changes and resetting of the changed status."""


class IComNativeDescriptorHandler:
    """Provides a top-level mapping layer between a COM object and a TypeDescriptor."""


class IComponent:
    """Provides functionality required by all components."""


class IContainer:
    """Provides functionality for containers. Containers are objects that logically contain zero or more components."""


class ICustomTypeDescriptor:
    """Provides an interface that supplies dynamic custom type information for an object."""


class IDataErrorInfo:
    """Provides the functionality to offer custom error information that a user interface can bind to."""


class IEditableObject:
    """Provides functionality to commit or rollback changes to an object that is used as a data source."""


class IExtenderProvider:
    """Defines the interface for extending properties to other components in a container."""


class IIntellisenseBuilder:
    """Provides an interface to facilitate the retrieval of the builder's name and to display the builder."""


class IListSource:
    """Provides functionality to an object to return a list that can be bound to a data source."""


class INestedContainer:
    """Provides functionality for nested containers, which logically contain zero or more other components and are owned by a parent component."""


class INestedSite:
    """Provides the ability to retrieve the full nested name of a component."""


class INotifyDataErrorInfo:
    """Defines members that data entity classes can implement to provide custom synchronous and asynchronous validation support."""


class INotifyPropertyChanged:
    """Notifies clients that a property value has changed."""


class INotifyPropertyChanging:
    """Notifies clients that a property value is changing."""


class IRaiseItemChangedEvents:
    """Indicates whether a class converts property change events to ListChanged events."""


class IRevertibleChangeTracking:
    """Provides support for rolling back the changes."""


class ISite:
    """Provides functionality required by sites."""


class ISupportInitialize:
    """Specifies that this object supports a simple, transacted notification for batch initialization."""


class ISupportInitializeNotification:
    """Allows coordination of initialization for a component and its dependent properties."""


class ISynchronizeInvoke:
    """Provides a way to synchronously or asynchronously execute a delegate."""


class ITypeDescriptorContext:
    """Provides contextual information about a component, such as its container and property descriptor."""


class ITypedList:
    """Provides functionality to discover the schema for a bindable list, where the properties available for binding differ from the public properties of the object to bind to."""


# ---------- ENUMS ---------- #

class BindableSupport:
    """Specifies values to indicate whether a property can be bound to a data element or another property."""


class BindingDirection:
    """Specifies whether the template can be bound one way or two ways."""


class CollectionChangeAction:
    """Specifies how the collection is changed."""


class DataObjectMethodType:
    """Identifies the type of data operation performed by a method, as specified by the DataObjectMethodAttribute applied to the method."""


class DesignerSerializationVisibility:
    """Specifies the visibility a property has to the design-time serializer."""


class EditorBrowsableState:
    """Specifies the browsable state of a property or method from within an editor."""


class InheritanceLevel:
    """Defines identifiers for types of inheritance levels."""


class LicenseUsageMode:
    """Specifies when the License can be used."""


class ListChangedType:
    """Specifies how the list changed."""


class ListSortDirection:
    """Specifies the direction of a sort operation."""


class MaskedTextResultHint:
    """Specifies values that succinctly describe the results of a masked text parsing operation."""


class PropertyTabScope:
    """Defines identifiers that indicate the persistence scope of a tab in the Properties window."""


class RefreshProperties:
    """Defines identifiers that indicate the type of a refresh of the Properties window."""


class ToolboxItemFilterType:
    """Defines identifiers used to indicate the type of filter that a ToolboxItemFilterAttribute uses."""


# ---------- DELEGATES ---------- #

class AddingNewEventHandler:
    """Represents the method that will handle the AddingNew event."""


class AsyncCompletedEventHandler:
    """Represents the method that will handle the MethodNameCompleted event of an asynchronous operation."""


class CancelEventHandler:
    """Represents the method that handles a cancelable event."""


class CollectionChangeEventHandler:
    """Represents the method that handles the CollectionChanged event raised when adding elements to or removing elements from a collection."""


class DoWorkEventHandler:
    """Represents the method that will handle the DoWork event. This class cannot be inherited."""


class HandledEventHandler:
    """Represents a method that can handle events which may or may not require further processing after the event handler has returned."""


class ListChangedEventHandler:
    """Represents the method that will handle the ListChanged event of the IBindingList class."""


class ProgressChangedEventHandler:
    """Represents the method that will handle the ProgressChanged event of the BackgroundWorker class. This class cannot be inherited."""


class PropertyChangedEventHandler:
    """Represents the method that will handle the PropertyChanged event raised when a property is changed on a component."""


class PropertyChangingEventHandler:
    """Represents the method that will handle the PropertyChanging event of an INotifyPropertyChanging interface."""


class RefreshEventHandler:
    """Represents the method that handles the Refreshed event raised when a Type or component is changed during design time."""


class RunWorkerCompletedEventHandler:
    """Represents the method that will handle the RunWorkerCompleted event of a BackgroundWorker class."""
