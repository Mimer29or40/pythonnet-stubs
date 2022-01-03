__all__ = [
    'ValueSerializerAttribute',
]

from typing import overload

from System import Attribute, StringType, Type, String


# ---------- CLASSES ---------- #

class ValueSerializerAttribute(Attribute):
    """Identifies the ValueSerializer class that a type or property should
    use when it is serialized.
    """
    
    @overload
    def __init__(self, valueSerializerTypeName: StringType):
        """Initializes a new instance of the ValueSerializerAttribute class,
        using an assembly qualified type name string.
        """
    
    @overload
    def __init__(self, valueSerializerType: Type):
        """Initializes a new instance of the ValueSerializerAttribute class,
        using the specified type.
        """
    
    @property
    def ValueSerializerType(self) -> Type:
        """Gets the type of the ValueSerializer class reported by this attribute."""
    
    @property
    def ValueSerializerTypeName(self) -> String:
        """Gets the assembly qualified name of the ValueSerializer type for this type or property."""
