__all__ = [
    'AssemblyDependencyResolver',
    'AssemblyLoadContext',
]


# TODO

# ---------- CLASSES ---------- #

class AssemblyDependencyResolver:
    """Allows a program to resolve assemblies and native libraries to paths based on the dependencies of a given assembly."""


class AssemblyLoadContext:
    """Represents the runtime's concept of a scope for assembly loading."""
    
    # ---------- STRUCTS ---------- #
    
    class ContextualReflectionScope:
        """Provides a return type used exclusively for EnterContextualReflection(). It is intended to be used as an IDisposable in a using block."""
