__all__ = [
    'AssociatedMetadataTypeTypeDescriptionProvider',
    'AssociationAttribute',
    'CompareAttribute',
    'ConcurrencyCheckAttribute',
    'CreditCardAttribute',
    'CustomValidationAttribute',
    'DataTypeAttribute',
    'DisplayAttribute',
    'DisplayColumnAttribute',
    'DisplayFormatAttribute',
    'EditableAttribute',
    'EmailAddressAttribute',
    'EnumDataTypeAttribute',
    'FileExtensionsAttribute',
    'FilterUIHintAttribute',
    'KeyAttribute',
    'MaxLengthAttribute',
    'MetadataTypeAttribute',
    'MinLengthAttribute',
    'PhoneAttribute',
    'RangeAttribute',
    'RegularExpressionAttribute',
    'RequiredAttribute',
    'ScaffoldColumnAttribute',
    'StringLengthAttribute',
    'TimestampAttribute',
    'UIHintAttribute',
    'UrlAttribute',
    'ValidationAttribute',
    'ValidationContext',
    'ValidationException',
    'ValidationResult',
    'Validator',
    'IValidatableObject',
    'DataType',
]


# TODO

# ---------- CLASSES ---------- #

class AssociatedMetadataTypeTypeDescriptionProvider:
    """Extends the metadata information for a class by adding attributes and property information that is defined in an associated class."""


class AssociationAttribute:
    """Specifies that an entity member represents a data relationship, such as a foreign key relationship."""


class CompareAttribute:
    """Provides an attribute that compares two properties."""


class ConcurrencyCheckAttribute:
    """Specifies that a property participates in optimistic concurrency checks."""


class CreditCardAttribute:
    """Specifies that a data field value is a credit card number."""


class CustomValidationAttribute:
    """Specifies a custom validation method that is used to validate a property or class instance."""


class DataTypeAttribute:
    """Specifies the name of an additional type to associate with a data field."""


class DisplayAttribute:
    """Provides a general-purpose attribute that lets you specify localizable strings for types and members of entity partial classes."""


class DisplayColumnAttribute:
    """Specifies the column that is displayed in the referred table as a foreign-key column."""


class DisplayFormatAttribute:
    """Specifies how data fields are displayed and formatted by ASP.NET Dynamic Data."""


class EditableAttribute:
    """Indicates whether a data field is editable."""


class EmailAddressAttribute:
    """Validates an email address."""


class EnumDataTypeAttribute:
    """Enables a .NET enumeration to be mapped to a data column."""


class FileExtensionsAttribute:
    """Validates file name extensions."""


class FilterUIHintAttribute:
    """Represents an attribute that is used to specify the filtering behavior for a column."""


class KeyAttribute:
    """Denotes one or more properties that uniquely identify an entity."""


class MaxLengthAttribute:
    """Specifies the maximum length of array or string data allowed in a property."""


class MetadataTypeAttribute:
    """Specifies the metadata class to associate with a data model class."""


class MinLengthAttribute:
    """Specifies the minimum length of array or string data allowed in a property."""


class PhoneAttribute:
    """Specifies that a data field value is a well-formed phone number."""


class RangeAttribute:
    """Specifies the numeric range constraints for the value of a data field."""


class RegularExpressionAttribute:
    """Specifies that a data field value in ASP.NET Dynamic Data must match the specified regular expression."""


class RequiredAttribute:
    """Specifies that a data field value is required."""


class ScaffoldColumnAttribute:
    """Specifies whether a class or data column uses scaffolding."""


class StringLengthAttribute:
    """Specifies the minimum and maximum length of characters that are allowed in a data field."""


class TimestampAttribute:
    """Specifies the data type of the column as a row version."""


class UIHintAttribute:
    """Specifies the template or user control that Dynamic Data uses to display a data field."""


class UrlAttribute:
    """Provides URL validation."""


class ValidationAttribute:
    """Serves as the base class for all validation attributes."""


class ValidationContext:
    """Describes the context in which a validation check is performed."""


class ValidationException:
    """Represents the exception that occurs during validation of a data field when the ValidationAttribute class is used."""


class ValidationResult:
    """Represents a container for the results of a validation request."""


class Validator:
    """Defines a helper class that can be used to validate objects, properties, and methods when it is included in their associated ValidationAttribute attributes."""


# ---------- INTERFACES ---------- #

class IValidatableObject:
    """Provides a way for an object to be validated."""


# ---------- ENUMS ---------- #

class DataType:
    """Represents an enumeration of the data types associated with data fields and parameters."""
