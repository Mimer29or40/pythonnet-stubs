__all__ = [
    'ColorConverter',
    'ColorTranslator',
    'PointConverter',
    'RectangleConverter',
    'SizeConverter',
    'SizeFConverter',
    'SystemColors',
    'Color',
    'Point',
    'PointF',
    'Rectangle',
    'RectangleF',
    'Size',
    'SizeF',
    'KnownColor',
]


# TODO

# ---------- CLASSES ---------- #

class ColorConverter:
    """Converts colors from one data type to another. Access this class through the TypeDescriptor."""

class ColorTranslator:
    """Translates colors to and from GDI+ Color structures. This class cannot be inherited."""

class PointConverter:
    """Converts a Point object from one data type to another."""

class RectangleConverter:
    """Converts rectangles from one data type to another. Access this class through the TypeDescriptor."""

class SizeConverter:
    """The SizeConverter class is used to convert from one data type to another. Access this class through the TypeDescriptor object."""

class SizeFConverter:
    """Converts SizeF objects from one type to another."""

class SystemColors:
    """Each property of the SystemColors class is a Color structure that is the color of a Windows display element."""


# ---------- STRUCTS ---------- #

class Color:
    """Represents an ARGB (alpha, red, green, blue) color."""

class Point:
    """Represents an ordered pair of integer x- and y-coordinates that defines a point in a two-dimensional plane."""

class PointF:
    """Represents an ordered pair of floating-point x- and y-coordinates that defines a point in a two-dimensional plane."""

class Rectangle:
    """Stores a set of four integers that represent the location and size of a rectangle."""

class RectangleF:
    """Stores a set of four floating-point numbers that represent the location and size of a rectangle. For more advanced region functions, use a Region object."""

class Size:
    """Stores an ordered pair of integers, which specify a Height and Width."""

class SizeF:
    """Stores an ordered pair of floating-point numbers, typically the width and height of a rectangle."""


# ---------- ENUMS ---------- #

class KnownColor:
    """Specifies the known system colors."""
