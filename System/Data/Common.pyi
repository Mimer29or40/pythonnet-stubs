__all__ = [
    'DataAdapter',
    'DataColumnMapping',
    'DataColumnMappingCollection',
    'DataTableMapping',
    'DataTableMappingCollection',
    'DbBatch',
    'DbBatchCommand',
    'DbBatchCommandCollection',
    'DbColumn',
    'DbCommand',
    'DbCommandBuilder',
    'DbConnection',
    'DbConnectionStringBuilder',
    'DbDataAdapter',
    'DbDataReader',
    'DbDataReaderExtensions',
    'DbDataRecord',
    'DbDataSourceEnumerator',
    'DbEnumerator',
    'DbException',
    'DbMetaDataCollectionNames',
    'DbMetaDataColumnNames',
    'DbParameter',
    'DbParameterCollection',
    'DbProviderFactories',
    'DbProviderFactory',
    'DbProviderSpecificTypePropertyAttribute',
    'DbTransaction',
    'RowUpdatedEventArgs',
    'RowUpdatingEventArgs',
    'SchemaTableColumn',
    'SchemaTableOptionalColumn',
    'IDbColumnSchemaGenerator',
    'CatalogLocation',
    'GroupByBehavior',
    'IdentifierCase',
    'SupportedJoinOperators',
]


# TODO

# ---------- CLASSES ---------- #

class DataAdapter:
    """Represents a set of SQL commands and a database connection that are used to fill the DataSet and update the data source."""


class DataColumnMapping:
    """Contains a generic column mapping for an object that inherits from DataAdapter. This class cannot be inherited."""


class DataColumnMappingCollection:
    """Contains a collection of DataColumnMapping objects."""


class DataTableMapping:
    """Contains a description of a mapped relationship between a source table and a DataTable. This class is used by a DataAdapter when populating a DataSet."""


class DataTableMappingCollection:
    """A collection of DataTableMapping objects. This class cannot be inherited."""


class DbBatch:
    """"""


class DbBatchCommand:
    """"""


class DbBatchCommandCollection:
    """"""


class DbColumn:
    """Represents a column within a data source."""


class DbCommand:
    """Represents an SQL statement or stored procedure to execute against a data source. Provides a base class for database-specific classes that represent commands. ExecuteNonQueryAsync."""


class DbCommandBuilder:
    """Automatically generates single-table commands used to reconcile changes made to a DataSet with the associated database. This is an abstract class that can only be inherited."""


class DbConnection:
    """Defines the core behavior of database connections and provides a base class for database-specific connections."""


class DbConnectionStringBuilder:
    """Provides a base class for strongly typed connection string builders."""


class DbDataAdapter:
    """Aids implementation of the IDbDataAdapter interface. Inheritors of DbDataAdapter implement a set of functions to provide strong typing, but inherit most of the functionality needed to fully implement a DataAdapter."""


class DbDataReader:
    """Reads a forward-only stream of rows from a data source."""


class DbDataReaderExtensions:
    """This class contains column schema extension methods for DbDataReader."""


class DbDataRecord:
    """Implements IDataRecord and ICustomTypeDescriptor, and provides data binding support for DbEnumerator."""


class DbDataSourceEnumerator:
    """Provides a mechanism for enumerating all available instances of database servers within the local network."""


class DbEnumerator:
    """Exposes the GetEnumerator() method, which supports a simple iteration over a collection by a .NET data provider."""


class DbException:
    """The base class for all exceptions thrown on behalf of the data source."""


class DbMetaDataCollectionNames:
    """Provides a list of constants for the well-known MetaDataCollections: DataSourceInformation, DataTypes, MetaDataCollections, ReservedWords, and Restrictions."""


class DbMetaDataColumnNames:
    """Provides static values that are used for the column names in the MetaDataCollection objects contained in the DataTable. The DataTable is created by the GetSchema method."""


class DbParameter:
    """Represents a parameter to a DbCommand and optionally, its mapping to a DataSet column. For more information on parameters, see Configuring Parameters and Parameter Data Types."""


class DbParameterCollection:
    """The base class for a collection of parameters relevant to a DbCommand."""


class DbProviderFactories:
    """Represents a set of static methods for creating one or more instances of DbProviderFactory classes."""


class DbProviderFactory:
    """Represents a set of methods for creating instances of a provider's implementation of the data source classes."""


class DbProviderSpecificTypePropertyAttribute:
    """Identifies which provider-specific property in the strongly typed parameter classes is to be used when setting a provider-specific type."""


class DbTransaction:
    """Defines the core behavior of database transactions and provides a base class for database-specific transactions."""


class RowUpdatedEventArgs:
    """Provides data for the RowUpdated event of a .NET data provider."""


class RowUpdatingEventArgs:
    """Provides the data for the RowUpdating event of a .NET data provider."""


class SchemaTableColumn:
    """Describes the column metadata of the schema for a database table."""


class SchemaTableOptionalColumn:
    """Describes optional column metadata of the schema for a database table."""


# ---------- INTERFACES ---------- #

class IDbColumnSchemaGenerator:
    """Generates a column schema."""


# ---------- ENUMS ---------- #

class CatalogLocation:
    """Indicates the position of the catalog name in a qualified table name in a text command."""


class GroupByBehavior:
    """Specifies the relationship between the columns in a GROUP BY clause and the non-aggregated columns in the select-list of a SELECT statement."""


class IdentifierCase:
    """Specifies how identifiers are treated by the data source when searching the system catalog."""


class SupportedJoinOperators:
    """Specifies what types of Transact-SQL join statements are supported by the data source."""
