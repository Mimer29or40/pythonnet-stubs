__all__ = [
    'CodedIndex',
    'ControlFlowBuilder',
    'ExportedTypeExtensions',
    'MetadataAggregator',
    'MetadataBuilder',
    'MetadataReaderExtensions',
    'MetadataRootBuilder',
    'MetadataSizes',
    'MetadataTokens',
    'PortablePdbBuilder',
    'ArrayShapeEncoder',
    'BlobEncoder',
    'CustomAttributeArrayTypeEncoder',
    'CustomAttributeElementTypeEncoder',
    'CustomAttributeNamedArgumentsEncoder',
    'CustomModifiersEncoder',
    'EditAndContinueLogEntry',
    'ExceptionRegionEncoder',
    'FixedArgumentsEncoder',
    'GenericTypeArgumentsEncoder',
    'InstructionEncoder',
    'LabelHandle',
    'LiteralEncoder',
    'LiteralsEncoder',
    'LocalVariablesEncoder',
    'LocalVariableTypeEncoder',
    'MethodBodyStreamEncoder',
    'MethodSignatureEncoder',
    'NamedArgumentsEncoder',
    'NamedArgumentTypeEncoder',
    'NameEncoder',
    'ParametersEncoder',
    'ParameterTypeEncoder',
    'PermissionSetEncoder',
    'ReturnTypeEncoder',
    'ScalarEncoder',
    'SignatureDecoder',
    'SignatureTypeEncoder',
    'VectorEncoder',
    'EditAndContinueOperation',
    'FunctionPointerAttributes',
    'HeapIndex',
    'MethodBodyAttributes',
    'TableIndex',
]

from typing import Generic, TypeVar

TType = TypeVar('TType')
TGenericContext = TypeVar('TGenericContext')


# TODO

# ---------- CLASSES ---------- #

class CodedIndex:
    """"""


class ControlFlowBuilder:
    """"""


class ExportedTypeExtensions:
    """Provides an extension method to access the TypeDefinitionId column of the ExportedType table."""


class MetadataAggregator:
    """"""


class MetadataBuilder:
    """The MetadataBuilder class reads and writes metadata for an assembly in a highly performant manner. It is designed for use by compilers and other assembly generation tools."""


class MetadataReaderExtensions:
    """Provides extension methods for working with certain raw elements of the ECMA-335 metadata tables and heaps."""


class MetadataRootBuilder:
    """Builder of a Metadata Root to be embedded in a Portable Executable image."""


class MetadataSizes:
    """Provides information on sizes of various metadata structures."""


class MetadataTokens:
    """"""


class PortablePdbBuilder:
    """Represents the builder of a Portable PDB image."""


# ---------- STRUCTS ---------- #

class ArrayShapeEncoder:
    """"""


class BlobEncoder:
    """"""


class CustomAttributeArrayTypeEncoder:
    """"""


class CustomAttributeElementTypeEncoder:
    """"""


class CustomAttributeNamedArgumentsEncoder:
    """"""


class CustomModifiersEncoder:
    """"""


class EditAndContinueLogEntry:
    """"""


class ExceptionRegionEncoder:
    """"""


class FixedArgumentsEncoder:
    """"""


class GenericTypeArgumentsEncoder:
    """"""


class InstructionEncoder:
    """Encodes instructions."""


class LabelHandle:
    """"""


class LiteralEncoder:
    """Provides methods for encoding literals."""


class LiteralsEncoder:
    """"""


class LocalVariablesEncoder:
    """"""


class LocalVariableTypeEncoder:
    """"""


class MethodBodyStreamEncoder:
    """Provides an encoder for a method body stream."""
    
    class MethodBody:
        """Describes a method body. This class is meant to used along with the MethodBodyStreamEncoder class."""


class MethodSignatureEncoder:
    """Provides an encoder for method signatures."""


class NamedArgumentsEncoder:
    """"""


class NamedArgumentTypeEncoder:
    """"""


class NameEncoder:
    """"""


class ParametersEncoder:
    """"""


class ParameterTypeEncoder:
    """"""


class PermissionSetEncoder:
    """"""


class ReturnTypeEncoder:
    """"""


class ScalarEncoder:
    """"""


class SignatureDecoder(Generic[TType, TGenericContext]):
    """Decodes signature blobs."""


class SignatureTypeEncoder:
    """"""


class VectorEncoder:
    """"""


# ---------- ENUMS ---------- #

class EditAndContinueOperation:
    """"""


class FunctionPointerAttributes:
    """"""


class HeapIndex:
    """"""


class MethodBodyAttributes:
    """Defines method body attributes."""


class TableIndex:
    """"""
