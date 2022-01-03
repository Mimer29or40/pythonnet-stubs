__all__ = [
    'MissingManifestResourceException',
    'MissingSatelliteAssemblyException',
    'NeutralResourcesLanguageAttribute',
    'ResourceManager',
    'ResourceReader',
    'ResourceSet',
    'ResourceWriter',
    'SatelliteContractVersionAttribute',
    'IResourceReader',
    'IResourceWriter',
    'UltimateResourceFallbackLocation',
]
# TODO

# ---------- CLASSES ---------- #

class MissingManifestResourceException:
    """The exception that is thrown if the main assembly does not contain the resources for the neutral culture, and an appropriate satellite assembly is missing."""

class MissingSatelliteAssemblyException:
    """The exception that is thrown when the satellite assembly for the resources of the default culture is missing."""

class NeutralResourcesLanguageAttribute:
    """Informs the resource manager of an app's default culture. This class cannot be inherited."""

class ResourceManager:
    """Represents a resource manager that provides convenient access to culture-specific resources at run time."""

class ResourceReader:
    """Enumerates the resources in a binary resources (.resources) file by reading sequential resource name/value pairs."""

class ResourceSet:
    """Stores all the resources localized for one particular culture, ignoring all other cultures, including any fallback rules."""

class ResourceWriter:
    """Writes resources in the system-default format to an output file or an output stream. This class cannot be inherited."""

class SatelliteContractVersionAttribute:
    """Instructs a ResourceManager object to ask for a particular version of a satellite assembly."""


# ---------- INTERFACES ---------- #

class IResourceReader:
    """Provides the base functionality for reading data from resource files."""

class IResourceWriter:
    """Provides the base functionality for writing resources to an output file or stream."""


# ---------- ENUMS ---------- #

class UltimateResourceFallbackLocation:
    """Specifies whether a ResourceManager object looks for the resources of the app's default culture in the main assembly or in a satellite assembly."""
