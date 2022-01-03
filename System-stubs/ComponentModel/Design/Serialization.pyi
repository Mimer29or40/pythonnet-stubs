__all__ = [
    'ComponentSerializationService',
    'ContextStack',
    'DefaultSerializationProviderAttribute',
    'DesignerLoader',
    'DesignerSerializerAttribute',
    'InstanceDescriptor',
    'MemberRelationshipService',
    'ResolveNameEventArgs',
    'RootDesignerSerializerAttribute',
    'SerializationStore',
    'MemberRelationship',
    'IDesignerLoaderHost',
    'IDesignerLoaderHost2',
    'IDesignerLoaderService',
    'IDesignerSerializationManager',
    'IDesignerSerializationProvider',
    'IDesignerSerializationService',
    'INameCreationService',
    'ResolveNameEventHandler',
]


# TODO

# ---------- CLASSES ---------- #

class ComponentSerializationService:
    """Provides the base class for serializing a set of components or serializable objects into a serialization store."""


class ContextStack:
    """Provides a stack object that can be used by a serializer to make information available to nested serializers."""


class DefaultSerializationProviderAttribute:
    """The DefaultSerializationProviderAttribute attribute is placed on a serializer to indicate the class to use as a default provider of that type of serializer."""


class DesignerLoader:
    """Provides a basic designer loader interface that can be used to implement a custom designer loader."""


class DesignerSerializerAttribute:
    """Indicates a serializer for the serialization manager to use to serialize the values of the type this attribute is applied to. This class cannot be inherited."""


class InstanceDescriptor:
    """Provides the information necessary to create an instance of an object. This class cannot be inherited."""


class MemberRelationshipService:
    """Provides the base class for relating one member to another."""


class ResolveNameEventArgs:
    """Provides data for the ResolveName event."""


class RootDesignerSerializerAttribute:
    """Indicates the base serializer to use for a root designer object. This class cannot be inherited."""


class SerializationStore:
    """Provides the base class for storing serialization data for the ComponentSerializationService."""


# ---------- STRUCTS ---------- #

class MemberRelationship:
    """Represents a single relationship between an object and a member."""


# ---------- INTERFACES ---------- #

class IDesignerLoaderHost:
    """Provides an interface that can extend a designer host to support loading from a serialized state."""


class IDesignerLoaderHost2:
    """Provides an interface that extends IDesignerLoaderHost to specify whether errors are tolerated while loading a design document."""


class IDesignerLoaderService:
    """Provides an interface that can extend a designer loader to support asynchronous loading of external components."""


class IDesignerSerializationManager:
    """Provides an interface that can manage design-time serialization."""


class IDesignerSerializationProvider:
    """Provides an interface that enables access to a serializer."""


class IDesignerSerializationService:
    """Provides an interface that can invoke serialization and deserialization."""


class INameCreationService:
    """Provides a service that can generate unique names for objects."""


# ---------- DELEGATES ---------- #

class ResolveNameEventHandler:
    """Represents the method that handles the ResolveName event of a serialization manager."""
