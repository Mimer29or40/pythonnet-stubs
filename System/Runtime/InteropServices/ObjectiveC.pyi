__all__ = [
    'ObjectiveCMarshal',
    'ObjectiveCTrackedTypeAttribute',
]


# TODO

# ---------- CLASSES ---------- #

class ObjectiveCMarshal:
    """API to enable Objective-C marshalling."""
    
    # ---------- ENUMS ---------- #
    
    class MessageSendFunction:
        """Objective-C msgSend function override options."""
    
    # ---------- DELEGATES ---------- #
    
    class UnhandledExceptionPropagationHandler:
        """Handler for unhandled Exceptions crossing the managed -> native boundary (that is, Reverse P/Invoke)."""


class ObjectiveCTrackedTypeAttribute:
    """Attribute used to indicate a class represents a tracked Objective-C type."""
