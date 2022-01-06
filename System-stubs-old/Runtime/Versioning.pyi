__all__ = [
    'ComponentGuaranteesAttribute',
    'FrameworkName',
    'OSPlatformAttribute',
    'RequiresPreviewFeaturesAttribute',
    'ResourceConsumptionAttribute',
    'ResourceExposureAttribute',
    'SupportedOSPlatformAttribute',
    'SupportedOSPlatformGuardAttribute',
    'TargetFrameworkAttribute',
    'TargetPlatformAttribute',
    'UnsupportedOSPlatformAttribute',
    'UnsupportedOSPlatformGuardAttribute',
    'VersioningHelper',
    'ComponentGuaranteesOptions',
    'ResourceScope',
]


# TODO

# ---------- CLASSES ---------- #

class ComponentGuaranteesAttribute:
    """Defines the compatibility guarantee of a component, type, or type member that may span multiple versions."""


class FrameworkName:
    """Represents the name of a version of .NET."""


class OSPlatformAttribute:
    """Base type for all platform-specific API attributes."""


class RequiresPreviewFeaturesAttribute:
    """Indicates that an API is in preview. This attribute allows call sites to be flagged with a diagnostic that indicates that a preview feature is used. Authors can use this attribute to ship preview features in their assemblies."""


class ResourceConsumptionAttribute:
    """Specifies the resource consumed by the member of a class. This class cannot be inherited."""


class ResourceExposureAttribute:
    """Specifies the resource exposure for a member of a class. This class cannot be inherited."""


class SupportedOSPlatformAttribute:
    """Indicates that an API is supported for a specified platform or operating system. If a version is specified, the API cannot be called from an earlier version. Multiple attributes can be applied to indicate support on multiple operating systems."""


class SupportedOSPlatformGuardAttribute:
    """Annotates a custom guard field, property or method with a supported platform name and optional version. Multiple attributes can be applied to indicate guard for multiple supported platforms."""


class TargetFrameworkAttribute:
    """Identifies the version of .NET that a particular assembly was compiled against."""


class TargetPlatformAttribute:
    """Specifies the operating system that a project targets, for example, Windows or iOS."""


class UnsupportedOSPlatformAttribute:
    """Marks APIs that were removed or are unsupported in a given operating system version."""


class UnsupportedOSPlatformGuardAttribute:
    """Annotates the custom guard field, property or method with an unsupported platform name and optional version. Multiple attributes can be applied to indicate guard for multiple unsupported platforms."""


class VersioningHelper:
    """Provides methods to aid developers in writing version-safe code. This class cannot be inherited."""


# ---------- ENUMS ---------- #

class ComponentGuaranteesOptions:
    """Describes the compatibility guarantee of a component, type, or type member that may span multiple versions."""


class ResourceScope:
    """Identifies the scope of a sharable resource."""
