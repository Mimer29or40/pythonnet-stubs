__all__ = [
    'BitOperations',
    'Vector',
    'BigInteger',
    'Complex',
    'Matrix3x2',
    'Matrix4x4',
    'Plane',
    'Quaternion',
    'Vector',
    'Vector2',
    'Vector3',
    'Vector4',
]

from typing import TypeVar, Generic

T = TypeVar('T')


# TODO

# ---------- CLASSES ---------- #

class BitOperations:
    """Provides utility methods for intrinsic bit-twiddling operations. The methods use hardware intrinsics when available on the underlying platform; otherwise, they use optimized software fallbacks."""


# ---------- STRUCTS ---------- #

class BigInteger:
    """Represents an arbitrarily large signed integer."""


class Complex:
    """Represents a complex number."""


class Matrix3x2:
    """Represents a 3x2 matrix."""


class Matrix4x4:
    """Represents a 4x4 matrix."""


class Plane:
    """Represents a plane in three-dimensional space."""


class Quaternion:
    """Represents a vector that is used to encode three-dimensional physical rotations."""


class Vector:
    """Provides a collection of static convenience methods for creating, manipulating, combining, and converting generic vectors."""


class Vector(Generic[T]):
    """Represents a single vector of a specified numeric type that is suitable for low-level optimization of parallel algorithms."""


class Vector2:
    """Represents a vector with two single-precision floating-point values."""


class Vector3:
    """Represents a vector with three single-precision floating-point values."""


class Vector4:
    """Represents a vector with four single-precision floating-point values."""
