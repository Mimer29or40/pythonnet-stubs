__all__ = [
    'ColumnAttribute',
    'ComplexTypeAttribute',
    'DatabaseGeneratedAttribute',
    'ForeignKeyAttribute',
    'InversePropertyAttribute',
    'NotMappedAttribute',
    'TableAttribute',
    'DatabaseGeneratedOption',
]


# TODO

# ---------- CLASSES ---------- #

class ColumnAttribute:
    """Represents the database column that a property is mapped to."""


class ComplexTypeAttribute:
    """Denotes that the class is a complex type. Complex types are non-scalar properties of entity types that enable scalar properties to be organized within entities. Complex types do not have keys and cannot be managed by the Entity Framework apart from the parent object."""


class DatabaseGeneratedAttribute:
    """Specifies how the database generates values for a property."""


class ForeignKeyAttribute:
    """Denotes a property used as a foreign key in a relationship."""


class InversePropertyAttribute:
    """Specifies the inverse of a navigation property that represents the other end of the same relationship."""


class NotMappedAttribute:
    """Denotes that a property or class should be excluded from database mapping."""


class TableAttribute:
    """Specifies the database table that a class is mapped to."""


# ---------- ENUMS ---------- #

class DatabaseGeneratedOption:
    """Represents the pattern used to generate values for a property in the database."""
