__all__ = [
    'CodeAccessSecurityAttribute',
    'SecurityAttribute',
    'SecurityPermissionAttribute',
    'PermissionState',
    'SecurityAction',
    'SecurityPermissionFlag',
]


# TODO

# ---------- CLASSES ---------- #

class CodeAccessSecurityAttribute:
    """Specifies the base attribute class for code access security."""


class SecurityAttribute:
    """Specifies the base attribute class for declarative security from which CodeAccessSecurityAttribute is derived."""


class SecurityPermissionAttribute:
    """Allows security actions for SecurityPermission to be applied to code using declarative security. This class cannot be inherited."""


# ---------- ENUMS ---------- #

class PermissionState:
    """Specifies whether a permission should have all or no access to resources at creation."""


class SecurityAction:
    """Specifies the security actions that can be performed using declarative security."""


class SecurityPermissionFlag:
    """Specifies access flags for the security permission object."""
