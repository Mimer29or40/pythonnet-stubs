__all__ = [
    'AllowNullAttribute',
    'DisallowNullAttribute',
    'DoesNotReturnAttribute',
    'DoesNotReturnIfAttribute',
    'DynamicallyAccessedMembersAttribute',
    'DynamicDependencyAttribute',
    'ExcludeFromCodeCoverageAttribute',
    'MaybeNullAttribute',
    'MaybeNullWhenAttribute',
    'MemberNotNullAttribute',
    'MemberNotNullWhenAttribute',
    'NotNullAttribute',
    'NotNullIfNotNullAttribute',
    'NotNullWhenAttribute',
    'RequiresAssemblyFilesAttribute',
    'RequiresUnreferencedCodeAttribute',
    'SuppressMessageAttribute',
    'UnconditionalSuppressMessageAttribute',
    'DynamicallyAccessedMemberTypes',
]


# TODO

# ---------- CLASSES ---------- #

class AllowNullAttribute:
    """Specifies that null is allowed as an input even if the corresponding type disallows it."""


class DisallowNullAttribute:
    """Specifies that null is disallowed as an input even if the corresponding type allows it."""


class DoesNotReturnAttribute:
    """Specifies that a method that will never return under any circumstance."""


class DoesNotReturnIfAttribute:
    """Specifies that the method will not return if the associated Boolean parameter is passed the specified value."""


class DynamicallyAccessedMembersAttribute:
    """Indicates that certain members on a specified Type are accessed dynamically, for example, through System.Reflection."""


class DynamicDependencyAttribute:
    """States a dependency that one member has on another."""


class ExcludeFromCodeCoverageAttribute:
    """Specifies that the attributed code should be excluded from code coverage information."""


class MaybeNullAttribute:
    """Specifies that an output may be null even if the corresponding type disallows it."""


class MaybeNullWhenAttribute:
    """Specifies that when a method returns ReturnValue, the parameter may be null even if the corresponding type disallows it."""


class MemberNotNullAttribute:
    """Specifies that the method or property will ensure that the listed field and property members have values that aren't null."""


class MemberNotNullWhenAttribute:
    """Specifies that the method or property will ensure that the listed field and property members have non-null values when returning with the specified return value condition."""


class NotNullAttribute:
    """Specifies that an output is not null even if the corresponding type allows it. Specifies that an input argument was not null when the call returns."""


class NotNullIfNotNullAttribute:
    """Specifies that the output will be non-null if the named parameter is non-null."""


class NotNullWhenAttribute:
    """Specifies that when a method returns ReturnValue, the parameter will not be null even if the corresponding type allows it."""


class RequiresAssemblyFilesAttribute:
    """Indicates that the specified member requires assembly files to be on disk."""


class RequiresUnreferencedCodeAttribute:
    """Indicates that the specified method requires dynamic access to code that is not referenced statically, for example, through System.Reflection."""


class SuppressMessageAttribute:
    """Suppresses reporting of a specific code analysis rule violation, allowing multiple suppressions on a single code artifact. Does not apply to compiler diagnostics."""


class UnconditionalSuppressMessageAttribute:
    """Suppresses reporting of a specific rule violation, allowing multiple suppressions on a single code artifact."""


# ---------- ENUMS ---------- #

class DynamicallyAccessedMemberTypes:
    """Specifies the types of members that are dynamically accessed. This enumeration has a FlagsAttribute attribute that allows a bitwise combination of its member values."""
