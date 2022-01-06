__all__ = [
    'ActiveDesignerEventArgs',
    'CheckoutException',
    'CommandID',
    'ComponentChangedEventArgs',
    'ComponentChangingEventArgs',
    'ComponentEventArgs',
    'ComponentRenameEventArgs',
    'DesignerCollection',
    'DesignerEventArgs',
    'DesignerOptionService',
    'DesignerOptionService',
    'DesignerTransaction',
    'DesignerTransactionCloseEventArgs',
    'DesignerVerb',
    'DesignerVerbCollection',
    'DesigntimeLicenseContext',
    'DesigntimeLicenseContextSerializer',
    'HelpKeywordAttribute',
    'MenuCommand',
    'ServiceContainer',
    'StandardCommands',
    'StandardToolWindows',
    'TypeDescriptionProviderService',
    'IComponentChangeService',
    'IComponentDiscoveryService',
    'IComponentInitializer',
    'IDesigner',
    'IDesignerEventService',
    'IDesignerFilter',
    'IDesignerHost',
    'IDesignerHostTransactionState',
    'IDesignerOptionService',
    'IDictionaryService',
    'IEventBindingService',
    'IExtenderListService',
    'IExtenderProviderService',
    'IHelpService',
    'IInheritanceService',
    'IMenuCommandService',
    'IReferenceService',
    'IResourceService',
    'IRootDesigner',
    'ISelectionService',
    'IServiceContainer',
    'ITreeDesigner',
    'ITypeDescriptorFilterService',
    'ITypeDiscoveryService',
    'ITypeResolutionService',
    'HelpContextType',
    'HelpKeywordType',
    'SelectionTypes',
    'ViewTechnology',
    'ActiveDesignerEventHandler',
    'ComponentChangedEventHandler',
    'ComponentChangingEventHandler',
    'ComponentEventHandler',
    'ComponentRenameEventHandler',
    'DesignerEventHandler',
    'DesignerTransactionCloseEventHandler',
    'ServiceCreatorCallback',
]


# TODO

# ---------- CLASSES ---------- #

class ActiveDesignerEventArgs:
    """Provides data for the ActiveDesigner event."""


class CheckoutException:
    """The exception that is thrown when an attempt to check out a file that is checked into a source code management program is canceled or fails."""


class CommandID:
    """Represents a unique command identifier that consists of a numeric command ID and a GUID menu group identifier."""


class ComponentChangedEventArgs:
    """Provides data for the ComponentChanged event. This class cannot be inherited."""


class ComponentChangingEventArgs:
    """Provides data for the ComponentChanging event. This class cannot be inherited."""


class ComponentEventArgs:
    """Provides data for the ComponentAdded, ComponentAdding, ComponentRemoved, and ComponentRemoving events."""


class ComponentRenameEventArgs:
    """Provides data for the ComponentRename event."""


class DesignerCollection:
    """Represents a collection of designers."""


class DesignerEventArgs:
    """Provides data for the DesignerCreated and DesignerDisposed events."""


class DesignerOptionService:
    """Provides a base class for getting and setting option values for a designer."""
    
    class DesignerOptionCollection:
        """Contains a collection of designer options. This class cannot be inherited."""


class DesignerTransaction:
    """Provides a way to group a series of design-time actions to improve performance and enable most types of changes to be undone."""


class DesignerTransactionCloseEventArgs:
    """Provides data for the TransactionClosed and TransactionClosing events."""


class DesignerVerb:
    """Represents a verb that can be invoked from a designer."""


class DesignerVerbCollection:
    """Represents a collection of DesignerVerb objects."""


class DesigntimeLicenseContext:
    """Represents a design-time license context that can support a license provider at design time."""


class DesigntimeLicenseContextSerializer:
    """Provides support for design-time license context serialization."""


class HelpKeywordAttribute:
    """Specifies the context keyword for a class or member. This class cannot be inherited."""


class MenuCommand:
    """Represents a Windows menu or toolbar command item."""


class ServiceContainer:
    """Provides a simple implementation of the IServiceContainer interface. This class cannot be inherited."""


class StandardCommands:
    """Defines identifiers for the standard set of commands that are available to most applications."""


class StandardToolWindows:
    """Defines GUID identifiers that correspond to the standard set of tool windows that are available in the design environment."""


class TypeDescriptionProviderService:
    """Provides a type description provider for a specified type."""


# ---------- INTERFACES ---------- #

class IComponentChangeService:
    """Provides an interface to add and remove the event handlers for events that add, change, remove or rename components, and provides methods to raise a ComponentChanged or ComponentChanging event."""


class IComponentDiscoveryService:
    """Enables enumeration of components at design time."""


class IComponentInitializer:
    """Provides a set of recommended default values during component creation."""


class IDesigner:
    """Provides the basic framework for building a custom designer."""


class IDesignerEventService:
    """Provides event notifications when root designers are added and removed, when a selected component changes, and when the current root designer changes."""


class IDesignerFilter:
    """Provides an interface that enables a designer to access and filter the dictionaries of a TypeDescriptor that stores the property, attribute, and event descriptors that a component designer can expose to the design-time environment."""


class IDesignerHost:
    """Provides an interface for managing designer transactions and components."""


class IDesignerHostTransactionState:
    """Specifies methods for the designer host to report on the state of transactions."""


class IDesignerOptionService:
    """Provides access to the designer options located on the Tools menu under the Options command in the Visual Studio development environment."""


class IDictionaryService:
    """Provides a basic, component site-specific, key-value pair dictionary through a service that a designer can use to store user-defined data."""


class IEventBindingService:
    """Provides a service for registering event handlers for component events."""


class IExtenderListService:
    """Provides an interface that can list extender providers."""


class IExtenderProviderService:
    """Provides an interface for adding and removing extender providers at design time."""


class IHelpService:
    """Provides methods for showing Help topics and adding and removing Help keywords at design time."""


class IInheritanceService:
    """Provides methods for identifying the components of a component."""


class IMenuCommandService:
    """Provides methods to manage the global designer verbs and menu commands available in design mode, and to show some types of shortcut menus."""


class IReferenceService:
    """Provides an interface for obtaining references to objects within a project by name or type, obtaining the name of a specified object, and for locating the parent of a specified object within a designer project."""


class IResourceService:
    """Provides an interface for designers to access resource readers and writers for specific CultureInfo resource types."""


class IRootDesigner:
    """Provides support for root-level designer view technologies."""


class ISelectionService:
    """Provides an interface for a designer to select components."""


class IServiceContainer:
    """Provides a container for services."""


class ITreeDesigner:
    """Provides support for building a set of related custom designers."""


class ITypeDescriptorFilterService:
    """Provides an interface to modify the set of member descriptors for a component in design mode."""


class ITypeDiscoveryService:
    """Discovers available types at design time."""


class ITypeResolutionService:
    """Provides an interface to retrieve an assembly or type by name."""


# ---------- ENUMS ---------- #

class HelpContextType:
    """Defines identifiers that indicate information about the context in which a request for Help information originated."""


class HelpKeywordType:
    """Defines identifiers that indicate the type of a Help keyword."""


class SelectionTypes:
    """Defines identifiers that indicate the type of a selection."""


class ViewTechnology:
    """Defines identifiers for a set of technologies that designer hosts support."""


# ---------- DELEGATES ---------- #

class ActiveDesignerEventHandler:
    """Represents the method that will handle the ActiveDesignerChanged event."""


class ComponentChangedEventHandler:
    """Represents the method that will handle a ComponentChanged event."""


class ComponentChangingEventHandler:
    """Represents the method that will handle a ComponentChanging event."""


class ComponentEventHandler:
    """Represents the method that will handle the ComponentAdding, ComponentAdded, ComponentRemoving, and ComponentRemoved events raised for component-level events."""


class ComponentRenameEventHandler:
    """Represents the method that will handle a ComponentRename event."""


class DesignerEventHandler:
    """Represents the method that will handle the DesignerCreated and DesignerDisposed events that are raised when a document is created or disposed of."""


class DesignerTransactionCloseEventHandler:
    """Represents the method that handles the TransactionClosed and TransactionClosing events of a designer."""


class ServiceCreatorCallback:
    """Provides a callback mechanism that can create an instance of a service on demand."""
