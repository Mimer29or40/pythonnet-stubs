__all__ = [
    'AssemblyExtensions',
    'BlobBuilder',
    'DebugMetadataHeader',
    'HandleComparer',
    'ILOpCodeExtensions',
    'ImageFormatLimitationException',
    'MetadataReader',
    'MetadataReaderProvider',
    'MetadataStringDecoder',
    'MetadataUpdateHandlerAttribute',
    'MetadataUpdater',
    'MethodBodyBlock',
    'PEReaderExtensions',
    'ArrayShape',
    'AssemblyDefinition',
    'AssemblyDefinitionHandle',
    'AssemblyFile',
    'AssemblyFileHandle',
    'AssemblyFileHandleCollection',
    'AssemblyReference',
    'AssemblyReferenceHandle',
    'AssemblyReferenceHandleCollection',
    'Blob',
    'BlobContentId',
    'BlobHandle',
    'BlobReader',
    'BlobWriter',
    'Constant',
    'ConstantHandle',
    'CustomAttribute',
    'CustomAttributeHandle',
    'CustomAttributeHandleCollection',
    'CustomAttributeNamedArgument',
    'CustomAttributeTypedArgument',
    'CustomAttributeValue',
    'CustomDebugInformation',
    'CustomDebugInformationHandle',
    'CustomDebugInformationHandleCollection',
    'DeclarativeSecurityAttribute',
    'DeclarativeSecurityAttributeHandle',
    'DeclarativeSecurityAttributeHandleCollection',
    'Document',
    'DocumentHandle',
    'DocumentHandleCollection',
    'DocumentNameBlobHandle',
    'EntityHandle',
    'EventAccessors',
    'EventDefinition',
    'EventDefinitionHandle',
    'EventDefinitionHandleCollection',
    'ExceptionRegion',
    'ExportedType',
    'ExportedTypeHandle',
    'ExportedTypeHandleCollection',
    'FieldDefinition',
    'FieldDefinitionHandle',
    'FieldDefinitionHandleCollection',
    'GenericParameter',
    'GenericParameterConstraint',
    'GenericParameterConstraintHandle',
    'GenericParameterConstraintHandleCollection',
    'GenericParameterHandle',
    'GenericParameterHandleCollection',
    'GuidHandle',
    'Handle',
    'ImportDefinition',
    'ImportDefinitionCollection',
    'ImportScope',
    'ImportScopeCollection',
    'ImportScopeHandle',
    'InterfaceImplementation',
    'InterfaceImplementationHandle',
    'InterfaceImplementationHandleCollection',
    'LocalConstant',
    'LocalConstantHandle',
    'LocalConstantHandleCollection',
    'LocalScope',
    'LocalScopeHandle',
    'LocalScopeHandleCollection',
    'LocalVariable',
    'LocalVariableHandle',
    'LocalVariableHandleCollection',
    'ManifestResource',
    'ManifestResourceHandle',
    'ManifestResourceHandleCollection',
    'MemberReference',
    'MemberReferenceHandle',
    'MemberReferenceHandleCollection',
    'MetadataStringComparer',
    'MethodDebugInformation',
    'MethodDebugInformationHandle',
    'MethodDebugInformationHandleCollection',
    'MethodDefinition',
    'MethodDefinitionHandle',
    'MethodDefinitionHandleCollection',
    'MethodImplementation',
    'MethodImplementationHandle',
    'MethodImplementationHandleCollection',
    'MethodImport',
    'MethodSignature',
    'MethodSpecification',
    'MethodSpecificationHandle',
    'ModuleDefinition',
    'ModuleDefinitionHandle',
    'ModuleReference',
    'ModuleReferenceHandle',
    'NamespaceDefinition',
    'NamespaceDefinitionHandle',
    'Parameter',
    'ParameterHandle',
    'ParameterHandleCollection',
    'PropertyAccessors',
    'PropertyDefinition',
    'PropertyDefinitionHandle',
    'PropertyDefinitionHandleCollection',
    'ReservedBlob',
    'SequencePoint',
    'SequencePointCollection',
    'SignatureHeader',
    'StandaloneSignature',
    'StandaloneSignatureHandle',
    'StringHandle',
    'TypeDefinition',
    'TypeDefinitionHandle',
    'TypeDefinitionHandleCollection',
    'TypeLayout',
    'TypeReference',
    'TypeReferenceHandle',
    'TypeReferenceHandleCollection',
    'TypeSpecification',
    'TypeSpecificationHandle',
    'UserStringHandle',
    'IConstructedTypeProvider',
    'ICustomAttributeTypeProvider',
    'ISignatureTypeProvider',
    'ISimpleTypeProvider',
    'ISZArrayTypeProvider',
]

from typing import TypeVar, Generic

TType = TypeVar('TType')
THandle = TypeVar('THandle')
TGenericContext = TypeVar('TGenericContext')


# TODO

# ---------- CLASSES ---------- #

class AssemblyExtensions:
    """"""


class BlobBuilder:
    """"""
    
    # ---------- STRUCTS ---------- #
    
    class Blobs:
        """"""


class DebugMetadataHeader:
    """"""


class HandleComparer:
    """"""


class ILOpCodeExtensions:
    """"""


class ImageFormatLimitationException:
    """The exception that is thrown when an attempt to write metadata exceeds a limit given by the format specification. For example, when the heap size limit is exceeded."""


class MetadataReader:
    """Reads metadata as defined by the ECMA 335 CLI specification."""


class MetadataReaderProvider:
    """Provides a MetadataReader for metadata stored in an array of bytes, a memory block, or a stream."""


class MetadataStringDecoder:
    """Provides the MetadataReader with a custom mechanism for decoding byte sequences in metadata that represent text."""


class MetadataUpdateHandlerAttribute:
    """Indicates that a type that should receive notifications of metadata updates."""


class MetadataUpdater:
    """"""


class MethodBodyBlock:
    """"""


class PEReaderExtensions:
    """"""


# ---------- STRUCTS ---------- #

class ArrayShape:
    """Represents the shape of an array type."""


class AssemblyDefinition:
    """"""


class AssemblyDefinitionHandle:
    """"""


class AssemblyFile:
    """"""


class AssemblyFileHandle:
    """"""


class AssemblyFileHandleCollection:
    """Represents a collection of AssemblyFileHandle."""
    
    class Enumerator:
        """"""


class AssemblyReference:
    """"""


class AssemblyReferenceHandle:
    """"""


class AssemblyReferenceHandleCollection:
    """A collection of assembly references."""
    
    class Enumerator:
        """"""


class Blob:
    """"""


class BlobContentId:
    """"""


class BlobHandle:
    """"""


class BlobReader:
    """"""


class BlobWriter:
    """"""


class Constant:
    """"""


class ConstantHandle:
    """"""


class CustomAttribute:
    """"""


class CustomAttributeHandle:
    """"""


class CustomAttributeHandleCollection:
    """"""
    
    class Enumerator:
        """"""


class CustomAttributeNamedArgument(Generic[TType]):
    """Represents a named argument decoded from a custom attribute signature."""


class CustomAttributeTypedArgument(Generic[TType]):
    """Represents a typed argument for a custom metadata attribute."""


class CustomAttributeValue(Generic[TType]):
    """Represents a custom attribute of the type specified by TType."""


class CustomDebugInformation:
    """"""


class CustomDebugInformationHandle:
    """"""


class CustomDebugInformationHandleCollection:
    """"""
    
    class Enumerator:
        """"""


class DeclarativeSecurityAttribute:
    """"""


class DeclarativeSecurityAttributeHandle:
    """"""


class DeclarativeSecurityAttributeHandleCollection:
    """"""
    
    class Enumerator:
        """"""


class Document:
    """The source document in the debug metadata."""


class DocumentHandle:
    """"""


class DocumentHandleCollection:
    """"""
    
    class Enumerator:
        """"""


class DocumentNameBlobHandle:
    """A BlobHandle representing a blob on #Blob heap in Portable PDB structured as Document Name."""


class EntityHandle:
    """Represents a metadata entity (such as a type reference, type definition, type specification, method definition, or custom attribute)."""


class EventAccessors:
    """"""


class EventDefinition:
    """"""


class EventDefinitionHandle:
    """"""


class EventDefinitionHandleCollection:
    """"""
    
    class Enumerator:
        """"""


class ExceptionRegion:
    """"""


class ExportedType:
    """"""


class ExportedTypeHandle:
    """"""


class ExportedTypeHandleCollection:
    """Represents a collection of TypeReferenceHandle instances."""
    
    class Enumerator:
        """"""


class FieldDefinition:
    """"""


class FieldDefinitionHandle:
    """"""


class FieldDefinitionHandleCollection:
    """"""
    
    class Enumerator:
        """"""


class GenericParameter:
    """"""


class GenericParameterConstraint:
    """"""


class GenericParameterConstraintHandle:
    """"""


class GenericParameterConstraintHandleCollection:
    """Represents a collection of constraints of a generic type parameter."""
    
    class Enumerator:
        """"""


class GenericParameterHandle:
    """"""


class GenericParameterHandleCollection:
    """Represents a collection of generic type parameters of a method or type."""
    
    class Enumerator:
        """"""


class GuidHandle:
    """"""


class Handle:
    """Represents any metadata entity (such as a type reference, a type definition, a type specification, a method definition, or a custom attribute) or value (a string, blob, guid, or user string)."""


class ImportDefinition:
    """"""


class ImportDefinitionCollection:
    """"""
    
    class Enumerator:
        """"""


class ImportScope:
    """Provides information about the lexical scope within which a group of imports are available. This information is stored in debug metadata."""


class ImportScopeCollection:
    """"""
    
    class Enumerator:
        """"""


class ImportScopeHandle:
    """"""


class InterfaceImplementation:
    """"""


class InterfaceImplementationHandle:
    """"""


class InterfaceImplementationHandleCollection:
    """"""
    
    class Enumerator:
        """"""


class LocalConstant:
    """Provides information about local constants. This information is stored in debug metadata."""


class LocalConstantHandle:
    """"""


class LocalConstantHandleCollection:
    """"""
    
    class Enumerator:
        """"""


class LocalScope:
    """Provides information about the scope of local variables and constants. This information is stored in debug metadata."""


class LocalScopeHandle:
    """"""


class LocalScopeHandleCollection:
    """"""
    
    class ChildrenEnumerator:
        """"""
    
    class Enumerator:
        """"""


class LocalVariable:
    """Provides information about local variables. This information is stored in debug metadata."""


class LocalVariableHandle:
    """"""


class LocalVariableHandleCollection:
    """"""
    
    class Enumerator:
        """"""


class ManifestResource:
    """"""


class ManifestResourceHandle:
    """"""


class ManifestResourceHandleCollection:
    """Represents a collection of ManifestResourceHandle instances."""
    
    class Enumerator:
        """"""


class MemberReference:
    """"""


class MemberReferenceHandle:
    """"""


class MemberReferenceHandleCollection:
    """Represents a collection of MemberReferenceHandle instances."""
    
    class Enumerator:
        """"""


class MetadataStringComparer:
    """Provides string comparison helpers to query strings in metadata while avoiding allocation if possible."""


class MethodDebugInformation:
    """Provides debug information associated with a method definition. This information is stored in debug metadata."""


class MethodDebugInformationHandle:
    """"""


class MethodDebugInformationHandleCollection:
    """"""
    
    class Enumerator:
        """"""


class MethodDefinition:
    """"""


class MethodDefinitionHandle:
    """"""


class MethodDefinitionHandleCollection:
    """"""
    
    class Enumerator:
        """"""


class MethodImplementation:
    """"""


class MethodImplementationHandle:
    """"""


class MethodImplementationHandleCollection:
    """"""
    
    class Enumerator:
        """"""


class MethodImport:
    """"""


class MethodSignature(Generic[TType]):
    """Represents a method (definition, reference, or standalone) or property signature. In the case of properties, the signature matches that of a getter with a distinguishing SignatureHeader."""


class MethodSpecification:
    """"""


class MethodSpecificationHandle:
    """"""


class ModuleDefinition:
    """"""


class ModuleDefinitionHandle:
    """"""


class ModuleReference:
    """"""


class ModuleReferenceHandle:
    """"""


class NamespaceDefinition:
    """"""


class NamespaceDefinitionHandle:
    """Provides a handle to a namespace definition."""


class Parameter:
    """"""


class ParameterHandle:
    """"""


class ParameterHandleCollection:
    """Contains a collection of parameters of a specified method."""
    
    class Enumerator:
        """"""


class PropertyAccessors:
    """"""


class PropertyDefinition:
    """"""


class PropertyDefinitionHandle:
    """"""


class PropertyDefinitionHandleCollection:
    """"""
    
    class Enumerator:
        """"""


class ReservedBlob(Generic[THandle]):
    """Represents a handle and a corresponding blob on a metadata heap that was reserved for future content update."""


class SequencePoint:
    """"""


class SequencePointCollection:
    """"""
    
    class Enumerator:
        """"""


class SignatureHeader:
    """Represents the signature characteristics specified by the leading byte of signature blobs."""


class StandaloneSignature:
    """"""


class StandaloneSignatureHandle:
    """"""


class StringHandle:
    """"""


class TypeDefinition:
    """"""


class TypeDefinitionHandle:
    """"""


class TypeDefinitionHandleCollection:
    """Contains a collection of TypeDefinitionHandle instances."""
    
    class Enumerator:
        """"""


class TypeLayout:
    """"""


class TypeReference:
    """"""


class TypeReferenceHandle:
    """"""


class TypeReferenceHandleCollection:
    """Contains a collection of TypeReferenceHandle instances."""
    
    class Enumerator:
        """"""


class TypeSpecification:
    """"""


class TypeSpecificationHandle:
    """"""


class UserStringHandle:
    """Represents a handle to the user string heap."""


# ---------- INTERFACES ---------- #

class IConstructedTypeProvider(Generic[TType]):
    """"""


class ICustomAttributeTypeProvider(Generic[TType]):
    """"""


class ISignatureTypeProvider(Generic[TType, TGenericContext]):
    """"""


class ISimpleTypeProvider(Generic[TType]):
    """"""


class ISZArrayTypeProvider(Generic[TType]):
    """"""
