__all__ = [
    'Extensions',
    'ValidationEventArgs',
    'XmlAtomicValue',
    'XmlSchema',
    'XmlSchemaAll',
    'XmlSchemaAnnotated',
    'XmlSchemaAnnotation',
    'XmlSchemaAny',
    'XmlSchemaAnyAttribute',
    'XmlSchemaAppInfo',
    'XmlSchemaAttribute',
    'XmlSchemaAttributeGroup',
    'XmlSchemaAttributeGroupRef',
    'XmlSchemaChoice',
    'XmlSchemaCollection',
    'XmlSchemaCollectionEnumerator',
    'XmlSchemaCompilationSettings',
    'XmlSchemaComplexContent',
    'XmlSchemaComplexContentExtension',
    'XmlSchemaComplexContentRestriction',
    'XmlSchemaComplexType',
    'XmlSchemaContent',
    'XmlSchemaContentModel',
    'XmlSchemaDatatype',
    'XmlSchemaDocumentation',
    'XmlSchemaElement',
    'XmlSchemaEnumerationFacet',
    'XmlSchemaException',
    'XmlSchemaExternal',
    'XmlSchemaFacet',
    'XmlSchemaFractionDigitsFacet',
    'XmlSchemaGroup',
    'XmlSchemaGroupBase',
    'XmlSchemaGroupRef',
    'XmlSchemaIdentityConstraint',
    'XmlSchemaImport',
    'XmlSchemaInclude',
    'XmlSchemaInference',
    'XmlSchemaInferenceException',
    'XmlSchemaInfo',
    'XmlSchemaKey',
    'XmlSchemaKeyref',
    'XmlSchemaLengthFacet',
    'XmlSchemaMaxExclusiveFacet',
    'XmlSchemaMaxInclusiveFacet',
    'XmlSchemaMaxLengthFacet',
    'XmlSchemaMinExclusiveFacet',
    'XmlSchemaMinInclusiveFacet',
    'XmlSchemaMinLengthFacet',
    'XmlSchemaNotation',
    'XmlSchemaNumericFacet',
    'XmlSchemaObject',
    'XmlSchemaObjectCollection',
    'XmlSchemaObjectEnumerator',
    'XmlSchemaObjectTable',
    'XmlSchemaParticle',
    'XmlSchemaPatternFacet',
    'XmlSchemaRedefine',
    'XmlSchemaSequence',
    'XmlSchemaSet',
    'XmlSchemaSimpleContent',
    'XmlSchemaSimpleContentExtension',
    'XmlSchemaSimpleContentRestriction',
    'XmlSchemaSimpleType',
    'XmlSchemaSimpleTypeContent',
    'XmlSchemaSimpleTypeList',
    'XmlSchemaSimpleTypeRestriction',
    'XmlSchemaSimpleTypeUnion',
    'XmlSchemaTotalDigitsFacet',
    'XmlSchemaType',
    'XmlSchemaUnique',
    'XmlSchemaValidationException',
    'XmlSchemaValidator',
    'XmlSchemaWhiteSpaceFacet',
    'XmlSchemaXPath',
    'IXmlSchemaInfo',
    'XmlSchemaContentProcessing',
    'XmlSchemaContentType',
    'XmlSchemaDatatypeVariety',
    'XmlSchemaDerivationMethod',
    'XmlSchemaForm',
    'XmlSchemaUse',
    'XmlSchemaValidationFlags',
    'XmlSchemaValidity',
    'XmlSeverityType',
    'XmlTypeCode',
    'ValidationEventHandler',
    'XmlValueGetter',
]


# TODO

# ---------- CLASSES ---------- #

class Extensions:
    """This class contains the LINQ to XML extension methods for XSD validation."""


class ValidationEventArgs:
    """Returns detailed information related to the ValidationEventHandler."""


class XmlAtomicValue:
    """Represents the typed value of a validated XML element or attribute. The XmlAtomicValue class cannot be inherited."""


class XmlSchema:
    """An in-memory representation of an XML Schema, as specified in the World Wide Web Consortium (W3C) XML Schema Part 1: Structures and XML Schema Part 2: Datatypes]."""


class XmlSchemaAll:
    """Represents the World Wide Web Consortium (W3C) all element (compositor)."""


class XmlSchemaAnnotated:
    """The base class for any element that can contain annotation elements."""


class XmlSchemaAnnotation:
    """Represents the World Wide Web Consortium (W3C) annotation element."""


class XmlSchemaAny:
    """Represents the World Wide Web Consortium (W3C) any element."""


class XmlSchemaAnyAttribute:
    """Represents the World Wide Web Consortium (W3C) anyAttribute element."""


class XmlSchemaAppInfo:
    """Represents the World Wide Web Consortium (W3C) appinfo element."""


class XmlSchemaAttribute:
    """Represents the attribute element from the XML Schema as specified by the World Wide Web Consortium (W3C). Attributes provide additional information for other document elements. The attribute tag is nested between the tags of a document's element for the schema. The XML document displays attributes as named items in the opening tag of an element."""


class XmlSchemaAttributeGroup:
    """Represents the attributeGroup element from the XML Schema as specified by the World Wide Web Consortium (W3C). AttributesGroups provides a mechanism to group a set of attribute declarations so that they can be incorporated as a group into complex type definitions."""


class XmlSchemaAttributeGroupRef:
    """Represents the attributeGroup element with the ref attribute from the XML Schema as specified by the World Wide Web Consortium (W3C). AttributesGroupRef is the reference for an attributeGroup, name property contains the attribute group being referenced."""


class XmlSchemaChoice:
    """Represents the choice element (compositor) from the XML Schema as specified by the World Wide Web Consortium (W3C). The choice allows only one of its children to appear in an instance."""


class XmlSchemaCollection:
    """Contains a cache of XML Schema definition language (XSD) and XML-Data Reduced (XDR) schemas. The XmlSchemaCollection class is obsolete. Use XmlSchemaSet instead."""


class XmlSchemaCollectionEnumerator:
    """Supports a simple iteration over a collection. This class cannot be inherited."""


class XmlSchemaCompilationSettings:
    """Provides schema compilation options for the XmlSchemaSet class This class cannot be inherited."""


class XmlSchemaComplexContent:
    """Represents the complexContent element from XML Schema as specified by the World Wide Web Consortium (W3C). This class represents the complex content model for complex types. It contains extensions or restrictions on a complex type that has either only elements or mixed content."""


class XmlSchemaComplexContentExtension:
    """Represents the extension element from XML Schema as specified by the World Wide Web Consortium (W3C). This class is for complex types with complex content model derived by extension. It extends the complex type by adding attributes or elements."""


class XmlSchemaComplexContentRestriction:
    """Represents the restriction element from XML Schema as specified by the World Wide Web Consortium (W3C). This class is for complex types with a complex content model derived by restriction. It restricts the contents of the complex type to a subset of the inherited complex type."""


class XmlSchemaComplexType:
    """Represents the complexType element from XML Schema as specified by the World Wide Web Consortium (W3C). This class defines a complex type that determines the set of attributes and content of an element."""


class XmlSchemaContent:
    """An abstract class for schema content."""


class XmlSchemaContentModel:
    """Specifies the order and structure of the child elements of a type."""


class XmlSchemaDatatype:
    """The XmlSchemaDatatype class is an abstract class for mapping XML Schema definition language (XSD) types to Common Language Runtime (CLR) types."""


class XmlSchemaDocumentation:
    """Represents the documentation element from XML Schema as specified by the World Wide Web Consortium (W3C). This class specifies information to be read or used by humans within an annotation."""


class XmlSchemaElement:
    """Represents the element element from XML Schema as specified by the World Wide Web Consortium (W3C). This class is the base class for all particle types and is used to describe an element in an XML document."""


class XmlSchemaEnumerationFacet:
    """Represents the enumeration facet from XML Schema as specified by the World Wide Web Consortium (W3C). This class specifies a list of valid values for a simpleType element. Declaration is contained within a restriction declaration."""


class XmlSchemaException:
    """Returns detailed information about the schema exception."""


class XmlSchemaExternal:
    """An abstract class. Provides information about the included schema."""


class XmlSchemaFacet:
    """Abstract class for all facets that are used when simple types are derived by restriction."""


class XmlSchemaFractionDigitsFacet:
    """Specifies a restriction on the number of digits that can be entered for the fraction value of a simpleType element. The value of fractionDigits must be a positive integer. Represents the World Wide Web Consortium (W3C) fractionDigits facet."""


class XmlSchemaGroup:
    """Represents the group element from XML Schema as specified by the World Wide Web Consortium (W3C). This class defines groups at the schema level that are referenced from the complex types. It groups a set of element declarations so that they can be incorporated as a group into complex type definitions."""


class XmlSchemaGroupBase:
    """An abstract class for XmlSchemaAll, XmlSchemaChoice, or XmlSchemaSequence."""


class XmlSchemaGroupRef:
    """Represents the group element with ref attribute from the XML Schema as specified by the World Wide Web Consortium (W3C). This class is used within complex types that reference a group defined at the schema level."""


class XmlSchemaIdentityConstraint:
    """Class for the identity constraints: key, keyref, and unique elements."""


class XmlSchemaImport:
    """Represents the import element from XML Schema as specified by the World Wide Web Consortium (W3C). This class is used to import schema components from other schemas."""


class XmlSchemaInclude:
    """Represents the include element from XML Schema as specified by the World Wide Web Consortium (W3C). This class is used to include declarations and definitions from an external schema. The included declarations and definitions are then available for processing in the containing schema."""


class XmlSchemaInference:
    """Infers an XML Schema Definition Language (XSD) schema from an XML document. The XmlSchemaInference class cannot be inherited."""
    
    class InferenceOption:
        """Affects occurrence and type information inferred by the XmlSchemaInference class for elements and attributes in an XML document."""


class XmlSchemaInferenceException:
    """Returns information about errors encountered by the XmlSchemaInference class while inferring a schema from an XML document."""


class XmlSchemaInfo:
    """Represents the post-schema-validation infoset of a validated XML node."""


class XmlSchemaKey:
    """This class represents the key element from XMLSchema as specified by the World Wide Web Consortium (W3C)."""


class XmlSchemaKeyref:
    """This class represents the keyref element from XMLSchema as specified by the World Wide Web Consortium (W3C)."""


class XmlSchemaLengthFacet:
    """Represents the length facet from XML Schema as specified by the World Wide Web Consortium (W3C). This class can be used to specify a restriction on the length of a simpleType element on the data type."""


class XmlSchemaMaxExclusiveFacet:
    """Represents the maxExclusive element from XML Schema as specified by the World Wide Web Consortium (W3C). This class can be used to specify a restriction on the maximum value of a simpleType element. The element value must be less than the value of the maxExclusive element."""


class XmlSchemaMaxInclusiveFacet:
    """Represents the maxInclusive element from XML Schema as specified by the World Wide Web Consortium (W3C). This class can be used to specify a restriction on the maximum value of a simpleType element. The element value must be less than or equal to the value of the maxInclusive element."""


class XmlSchemaMaxLengthFacet:
    """Represents the maxLength element from XML Schema as specified by the World Wide Web Consortium (W3C). This class can be used to specify a restriction on the maximum length of the data value of a simpleType element. The length must be less than the value of the maxLength element."""


class XmlSchemaMinExclusiveFacet:
    """Represents the minExclusive element from XML Schema as specified by the World Wide Web Consortium (W3C). This class can be used to specify a restriction on the minimum value of a simpleType element. The element value must be greater than the value of the minExclusive element."""


class XmlSchemaMinInclusiveFacet:
    """Represents the minInclusive element from XML Schema as specified by the World Wide Web Consortium (W3C). This class can be used to specify a restriction on the minimum value of a simpleType element. The element value must be greater than or equal to the value of the minInclusive element."""


class XmlSchemaMinLengthFacet:
    """Represents the minLength element from XML Schema as specified by the World Wide Web Consortium (W3C). This class can be used to specify a restriction on the minimum length of the data value of a simpleType element. The length must be greater than the value of the minLength element."""


class XmlSchemaNotation:
    """Represents the notation element from XML Schema as specified by the World Wide Web Consortium (W3C). An XML Schema notation declaration is a reconstruction of XML 1.0 NOTATION declarations. The purpose of notations is to describe the format of non-XML data within an XML document."""


class XmlSchemaNumericFacet:
    """Abstract class for defining numeric facets. This class is the base class for numeric facet classes such as XmlSchemaMinLengthFacet."""


class XmlSchemaObject:
    """Represents the root class for the Xml schema object model hierarchy and serves as a base class for classes such as the XmlSchema class."""


class XmlSchemaObjectCollection:
    """A collection of XmlSchemaObjects."""


class XmlSchemaObjectEnumerator:
    """Represents the enumerator for the XmlSchemaObjectCollection."""


class XmlSchemaObjectTable:
    """Provides the collections for contained elements in the XmlSchema class (for example, Attributes, AttributeGroups, Elements, and so on)."""


class XmlSchemaParticle:
    """Abstract class for that is the base class for all particle types (e.g. XmlSchemaAny)."""


class XmlSchemaPatternFacet:
    """Represents the pattern element from XML Schema as specified by the World Wide Web Consortium (W3C). This class can be used to specify a restriction on the value entered for a simpleType element."""


class XmlSchemaRedefine:
    """Represents the redefine element from XML Schema as specified by the World Wide Web Consortium (W3C). This class can be used to allow simple and complex types, groups and attribute groups from external schema files to be redefined in the current schema. This class can also be used to provide versioning for the schema elements."""


class XmlSchemaSequence:
    """Represents the sequence element (compositor) from the XML Schema as specified by the World Wide Web Consortium (W3C). The sequence requires the elements in the group to appear in the specified sequence within the containing element."""


class XmlSchemaSet:
    """Contains a cache of XML Schema definition language (XSD) schemas."""


class XmlSchemaSimpleContent:
    """Represents the simpleContent element from XML Schema as specified by the World Wide Web Consortium (W3C). This class is for simple and complex types with simple content model."""


class XmlSchemaSimpleContentExtension:
    """Represents the extension element for simple content from XML Schema as specified by the World Wide Web Consortium (W3C). This class can be used to derive simple types by extension. Such derivations are used to extend the simple type content of the element by adding attributes."""


class XmlSchemaSimpleContentRestriction:
    """Represents the restriction element for simple content from XML Schema as specified by the World Wide Web Consortium (W3C). This class can be used to derive simple types by restriction. Such derivations can be used to restrict the range of values for the element to a subset of the values specified in the inherited simple type."""


class XmlSchemaSimpleType:
    """Represents the simpleType element for simple content from XML Schema as specified by the World Wide Web Consortium (W3C). This class defines a simple type. Simple types can specify information and constraints for the value of attributes or elements with text-only content."""


class XmlSchemaSimpleTypeContent:
    """Abstract class for simple type content classes."""


class XmlSchemaSimpleTypeList:
    """Represents the list element from XML Schema as specified by the World Wide Web Consortium (W3C). This class can be used to define a simpleType element as a list of values of a specified data type."""


class XmlSchemaSimpleTypeRestriction:
    """Represents the restriction element for simple types from XML Schema as specified by the World Wide Web Consortium (W3C). This class can be used restricting simpleType element."""


class XmlSchemaSimpleTypeUnion:
    """Represents the union element for simple types from XML Schema as specified by the World Wide Web Consortium (W3C). A union datatype can be used to specify the content of a simpleType. The value of the simpleType element must be any one of a set of alternative datatypes specified in the union. Union types are always derived types and must comprise at least two alternative datatypes."""


class XmlSchemaTotalDigitsFacet:
    """Represents the totalDigits facet from XML Schema as specified by the World Wide Web Consortium (W3C). This class can be used to specify a restriction on the number of digits that can be entered for the value of a simpleType element. That value of totalDigits must be a positive integer."""


class XmlSchemaType:
    """The base class for all simple types and complex types."""


class XmlSchemaUnique:
    """Represents the unique element from XML Schema as specified by the World Wide Web Consortium (W3C). This class can be used to identify a unique constraint among a set of elements."""


class XmlSchemaValidationException:
    """Represents the exception thrown when XML Schema Definition Language (XSD) schema validation errors and warnings are encountered in an XML document being validated."""


class XmlSchemaValidator:
    """Represents an XML Schema Definition Language (XSD) Schema validation engine. The XmlSchemaValidator class cannot be inherited."""


class XmlSchemaWhiteSpaceFacet:
    """Represents the World Wide Web Consortium (W3C) whiteSpace facet."""


class XmlSchemaXPath:
    """Represents the World Wide Web Consortium (W3C) selector element."""


# ---------- INTERFACES ---------- #

class IXmlSchemaInfo:
    """Defines the post-schema-validation infoset of a validated XML node."""


# ---------- ENUMS ---------- #

class XmlSchemaContentProcessing:
    """Provides information about the validation mode of any and anyAttribute element replacements."""


class XmlSchemaContentType:
    """Enumerations for the content model of the complex type. This represents the content in the post-schema-validation information set (infoset)."""


class XmlSchemaDatatypeVariety:
    """Specifies the W3C XML schema data type variety of the type."""


class XmlSchemaDerivationMethod:
    """Provides different methods for preventing derivation."""


class XmlSchemaForm:
    """Indicates if attributes or elements need to be qualified with a namespace prefix."""


class XmlSchemaUse:
    """Indicator of how the attribute is used."""


class XmlSchemaValidationFlags:
    """Specifies schema validation options used by the XmlSchemaValidator and XmlReader classes."""


class XmlSchemaValidity:
    """Represents the validity of an XML item validated by the XmlSchemaValidator class."""


class XmlSeverityType:
    """Represents the severity of the validation event."""


class XmlTypeCode:
    """Represents the W3C XML Schema Definition Language (XSD) schema types."""


# ---------- DELEGATES ---------- #

class ValidationEventHandler:
    """Represents the callback method that will handle XML schema validation events and the ValidationEventArgs."""


class XmlValueGetter:
    """A delegate used by the XmlSchemaValidator class to pass attribute, text, and white space values as a Common Language Runtime (CLR) type compatible with the XML Schema Definition Language (XSD) type of the attribute, text, or white space."""
