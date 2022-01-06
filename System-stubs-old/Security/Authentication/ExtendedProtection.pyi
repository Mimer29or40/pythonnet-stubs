__all__ = [
    'ChannelBinding',
    'ExtendedProtectionPolicy',
    'ExtendedProtectionPolicyTypeConverter',
    'ServiceNameCollection',
    'ChannelBindingKind',
    'PolicyEnforcement',
    'ProtectionScenario',
]


# TODO

# ---------- CLASSES ---------- #

class ChannelBinding:
    """The ChannelBinding class encapsulates a pointer to the opaque data used to bind an authenticated transaction to a secure channel."""


class ExtendedProtectionPolicy:
    """The ExtendedProtectionPolicy class represents the extended protection policy used by the server to validate incoming client connections."""


class ExtendedProtectionPolicyTypeConverter:
    """The ExtendedProtectionPolicyTypeConverter class represents the type converter for extended protection policy used by the server to validate incoming client connections."""


class ServiceNameCollection:
    """The ServiceNameCollection class is a read-only collection of service principal names."""


# ---------- ENUMS ---------- #

class ChannelBindingKind:
    """The ChannelBindingKind enumeration represents the kinds of channel bindings that can be queried from secure channels."""


class PolicyEnforcement:
    """The PolicyEnforcement enumeration specifies when the ExtendedProtectionPolicy should be enforced."""


class ProtectionScenario:
    """The ProtectionScenario enumeration specifies the protection scenario enforced by the policy."""
