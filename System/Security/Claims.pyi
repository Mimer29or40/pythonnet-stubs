__all__ = [
    'Claim',
    'ClaimsIdentity',
    'ClaimsPrincipal',
    'ClaimTypes',
    'ClaimValueTypes',
]


# TODO

# ---------- CLASSES ---------- #

class Claim:
    """Represents a claim."""


class ClaimsIdentity:
    """Represents a claims-based identity."""


class ClaimsPrincipal:
    """An IPrincipal implementation that supports multiple claims-based identities."""


class ClaimTypes:
    """Defines constants for the well-known claim types that can be assigned to a subject. This class cannot be inherited."""


class ClaimValueTypes:
    """Defines claim value types according to the type URIs defined by W3C and OASIS. This class cannot be inherited."""
