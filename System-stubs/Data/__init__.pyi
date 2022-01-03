__all__ = [
    'Constraint',
    'ConstraintCollection',
    'ConstraintException',
    'DataColumn',
    'DataColumnChangeEventArgs',
    'DataColumnCollection',
    'DataException',
    'DataReaderExtensions',
    'DataRelation',
    'DataRelationCollection',
    'DataRow',
    'DataRowBuilder',
    'DataRowChangeEventArgs',
    'DataRowCollection',
    'DataRowComparer',
    'DataRowComparer',
    'DataRowExtensions',
    'DataRowView',
    'DataSet',
    'DataSysDescriptionAttribute',
    'DataTable',
    'DataTableClearEventArgs',
    'DataTableCollection',
    'DataTableExtensions',
    'DataTableNewRowEventArgs',
    'DataTableReader',
    'DataView',
    'DataViewManager',
    'DataViewSetting',
    'DataViewSettingCollection',
    'DBConcurrencyException',
    'DeletedRowInaccessibleException',
    'DuplicateNameException',
    'EnumerableRowCollection',
    'EnumerableRowCollection',
    'EnumerableRowCollectionExtensions',
    'EvaluateException',
    'FillErrorEventArgs',
    'ForeignKeyConstraint',
    'InRowChangingEventException',
    'InternalDataCollectionBase',
    'InvalidConstraintException',
    'InvalidExpressionException',
    'MergeFailedEventArgs',
    'MissingPrimaryKeyException',
    'NoNullAllowedException',
    'OrderedEnumerableRowCollection',
    'PropertyCollection',
    'ReadOnlyException',
    'RowNotInTableException',
    'StateChangeEventArgs',
    'StatementCompletedEventArgs',
    'StrongTypingException',
    'SyntaxErrorException',
    'TypedTableBase',
    'TypedTableBaseExtensions',
    'UniqueConstraint',
    'VersionNotFoundException',
    'IColumnMapping',
    'IColumnMappingCollection',
    'IDataAdapter',
    'IDataParameter',
    'IDataParameterCollection',
    'IDataReader',
    'IDataRecord',
    'IDbCommand',
    'IDbConnection',
    'IDbDataAdapter',
    'IDbDataParameter',
    'IDbTransaction',
    'ITableMapping',
    'ITableMappingCollection',
    'AcceptRejectRule',
    'CommandBehavior',
    'CommandType',
    'ConflictOption',
    'ConnectionState',
    'DataRowAction',
    'DataRowState',
    'DataRowVersion',
    'DataSetDateTime',
    'DataViewRowState',
    'DbType',
    'IsolationLevel',
    'KeyRestrictionBehavior',
    'LoadOption',
    'MappingType',
    'MissingMappingAction',
    'MissingSchemaAction',
    'ParameterDirection',
    'Rule',
    'SchemaSerializationMode',
    'SchemaType',
    'SerializationFormat',
    'SqlDbType',
    'StatementType',
    'UpdateRowSource',
    'UpdateStatus',
    'XmlReadMode',
    'XmlWriteMode',
    'DataColumnChangeEventHandler',
    'DataRowChangeEventHandler',
    'DataTableClearEventHandler',
    'DataTableNewRowEventHandler',
    'FillErrorEventHandler',
    'MergeFailedEventHandler',
    'StateChangeEventHandler',
    'StatementCompletedEventHandler',
]

from typing import TypeVar, Generic

T = TypeVar('T')
TRow = TypeVar('TRow')


# TODO

# ---------- CLASSES ---------- #

class Constraint:
    """Represents a constraint that can be enforced on one or more DataColumn objects."""


class ConstraintCollection:
    """Represents a collection of constraints for a DataTable."""


class ConstraintException:
    """Represents the exception that is thrown when attempting an action that violates a constraint."""


class DataColumn:
    """Represents the schema of a column in a DataTable."""


class DataColumnChangeEventArgs:
    """Provides data for the ColumnChanging event."""


class DataColumnCollection:
    """Represents a collection of DataColumn objects for a DataTable."""


class DataException:
    """Represents the exception that is thrown when errors are generated using ADO.NET components."""


class DataReaderExtensions:
    """Provides extension methods for DbDataReader."""


class DataRelation:
    """Represents a parent/child relationship between two DataTable objects."""


class DataRelationCollection:
    """Represents the collection of DataRelation objects for this DataSet."""


class DataRow:
    """Represents a row of data in a DataTable."""


class DataRowBuilder:
    """The DataRowBuilder type supports the .NET infrastructure and is not intended to be used directly from your code."""


class DataRowChangeEventArgs:
    """Provides data for the RowChanged, RowChanging, OnRowDeleting(DataRowChangeEventArgs), and OnRowDeleted(DataRowChangeEventArgs) events."""


class DataRowCollection:
    """Represents a collection of rows for a DataTable."""


class DataRowComparer:
    """Returns a singleton instance of the DataRowComparer<TRow> class."""


class DataRowComparer(Generic[TRow]):
    """Compares two DataRow objects for equivalence by using value-based comparison."""


class DataRowExtensions:
    """Defines the extension methods to the DataRow class. This is a static class."""


class DataRowView:
    """Represents a customized view of a DataRow."""


class DataSet:
    """Represents an in-memory cache of data."""


class DataSysDescriptionAttribute:
    """Marks a property, event, or extender with a description. Visual designers can display this description when referencing the member."""


class DataTable:
    """Represents one table of in-memory data."""


class DataTableClearEventArgs:
    """Provides data for the Clear() method."""


class DataTableCollection:
    """Represents the collection of tables for the DataSet."""


class DataTableExtensions:
    """Defines the extension methods to the DataTable class. DataTableExtensions is a static class."""


class DataTableNewRowEventArgs:
    """Provides data for the NewRow() method."""


class DataTableReader:
    """The DataTableReader obtains the contents of one or more DataTable objects in the form of one or more read-only, forward-only result sets."""


class DataView:
    """Represents a databindable, customized view of a DataTable for sorting, filtering, searching, editing, and navigation. The DataView does not store data, but instead represents a connected view of its corresponding DataTable. Changes to the DataView's data will affect the DataTable. Changes to the DataTable's data will affect all DataViews associated with it."""


class DataViewManager:
    """Contains a default DataViewSettingCollection for each DataTable in a DataSet."""


class DataViewSetting:
    """Represents the default settings for ApplyDefaultSort, DataViewManager, RowFilter, RowStateFilter, Sort, and Table for DataViews created from the DataViewManager."""


class DataViewSettingCollection:
    """Contains a read-only collection of DataViewSetting objects for each DataTable in a DataSet."""


class DBConcurrencyException:
    """The exception that is thrown by the DataAdapter during an insert, update, or delete operation if the number of rows affected equals zero."""


class DeletedRowInaccessibleException:
    """Represents the exception that is thrown when an action is tried on a DataRow that has been deleted."""


class DuplicateNameException:
    """Represents the exception that is thrown when a duplicate database object name is encountered during an add operation in a DataSet -related object."""


class EnumerableRowCollection:
    """Represents a collection of DataRow objects returned from a LINQ to DataSet query. This API supports the .NET infrastructure and is not intended to be used directly from your code."""


class EnumerableRowCollection(Generic[TRow]):
    """Represents a collection of DataRow objects returned from a query."""


class EnumerableRowCollectionExtensions:
    """Contains the extension methods for the data row collection classes."""


class EvaluateException:
    """Represents the exception that is thrown when the Expression property of a DataColumn cannot be evaluated."""


class FillErrorEventArgs:
    """Provides data for the FillError event of a DbDataAdapter."""


class ForeignKeyConstraint:
    """Represents an action restriction enforced on a set of columns in a primary key/foreign key relationship when a value or row is either deleted or updated."""


class InRowChangingEventException:
    """Represents the exception that is thrown when you call the EndEdit() method within the RowChanging event."""


class InternalDataCollectionBase:
    """Provides the base functionality for creating collections."""


class InvalidConstraintException:
    """Represents the exception that is thrown when incorrectly trying to create or access a relation."""


class InvalidExpressionException:
    """Represents the exception that is thrown when you try to add a DataColumn that contains an invalid Expression to a DataColumnCollection."""


class MergeFailedEventArgs:
    """Occurs when a target and source DataRow have the same primary key value, and the EnforceConstraints property is set to true."""


class MissingPrimaryKeyException:
    """Represents the exception that is thrown when you try to access a row in a table that has no primary key."""


class NoNullAllowedException:
    """Represents the exception that is thrown when you try to insert a null value into a column where AllowDBNull is set to false."""


class OrderedEnumerableRowCollection(Generic[TRow]):
    """Represents a collection of ordered DataRow objects returned from a query."""


class PropertyCollection:
    """Represents a collection of properties that can be added to DataColumn, DataSet, or DataTable."""


class ReadOnlyException:
    """Represents the exception that is thrown when you try to change the value of a read-only column."""


class RowNotInTableException:
    """Represents the exception that is thrown when you try to perform an operation on a DataRow that is not in a DataTable."""


class StateChangeEventArgs:
    """Provides data for the state change event of a .NET data provider."""


class StatementCompletedEventArgs:
    """Provides additional information for the StatementCompleted event."""


class StrongTypingException:
    """The exception that is thrown by a strongly typed DataSet when the user accesses a DBNull value."""


class SyntaxErrorException:
    """Represents the exception that is thrown when the Expression property of a DataColumn contains a syntax error."""


class TypedTableBase(Generic[T]):
    """This type is used as a base class for typed-DataTable object generation by Visual Studio and the XSD.exe .NET Framework tool, and is not intended to be used directly from your code."""


class TypedTableBaseExtensions:
    """Contains the extension methods for the TypedTableBase[T] class."""


class UniqueConstraint:
    """Represents a restriction on a set of columns in which all values must be unique."""


class VersionNotFoundException:
    """Represents the exception that is thrown when you try to return a version of a DataRow that has been deleted."""


# ---------- INTERFACES ---------- #

class IColumnMapping:
    """Associates a data source column with a DataSet column, and is implemented by the DataColumnMapping class, which is used in common by .NET data providers."""


class IColumnMappingCollection:
    """Contains a collection of DataColumnMapping objects, and is implemented by the DataColumnMappingCollection, which is used in common by .NET data providers."""


class IDataAdapter:
    """Allows an object to implement a DataAdapter, and represents a set of methods and mapping action-related properties that are used to fill and update a DataSet and update a data source.
    
    IDbDataAdapter instances are for data sources that are (or resemble) relational databases with textual commands (like Transact-SQL), while IDataAdapter instances could can use any type of data source.
    """


class IDataParameter:
    """Represents a parameter to a Command object, and optionally, its mapping to DataSet columns; and is implemented by .NET data providers that access data sources."""


class IDataParameterCollection:
    """Collects all parameters relevant to a Command object and their mappings to DataSet columns, and is implemented by .NET data providers that access data sources."""


class IDataReader:
    """Provides a means of reading one or more forward-only streams of result sets obtained by executing a command at a data source, and is implemented by .NET data providers that access relational databases."""


class IDataRecord:
    """Provides access to the column values within each row for a DataReader, and is implemented by .NET data providers that access relational databases."""


class IDbCommand:
    """Represents an SQL statement that is executed while connected to a data source, and is implemented by .NET data providers that access relational databases."""


class IDbConnection:
    """Represents an open connection to a data source, and is implemented by .NET data providers that access relational databases."""


class IDbDataAdapter:
    """Represents a set of command-related properties that are used to fill the DataSet and update a data source, and is implemented by .NET data providers that access relational databases."""


class IDbDataParameter:
    """Used by the Visual Basic .NET Data Designers to represent a parameter to a Command object, and optionally, its mapping to DataSet columns."""


class IDbTransaction:
    """Represents a transaction to be performed at a data source, and is implemented by .NET data providers that access relational databases."""


class ITableMapping:
    """Associates a source table with a table in a DataSet, and is implemented by the DataTableMapping class, which is used in common by .NET data providers."""


class ITableMappingCollection:
    """Contains a collection of TableMapping objects, and is implemented by the DataTableMappingCollection, which is used in common by .NET data providers."""


# ---------- ENUMS ---------- #

class AcceptRejectRule:
    """Determines the action that occurs when the AcceptChanges() or RejectChanges() method is invoked on a DataTable with a ForeignKeyConstraint."""


class CommandBehavior:
    """Provides a description of the results of the query and its effect on the database."""


class CommandType:
    """Specifies how a command string is interpreted."""


class ConflictOption:
    """Specifies how conflicting changes to the data source will be detected and resolved."""


class ConnectionState:
    """Describes the current state of the connection to a data source."""


class DataRowAction:
    """Describes an action performed on a DataRow."""


class DataRowState:
    """Gets the state of a DataRow object."""


class DataRowVersion:
    """Describes the version of a DataRow."""


class DataSetDateTime:
    """Describes the serialization format for DateTime columns in a DataSet."""


class DataViewRowState:
    """Describes the version of data in a DataRow."""


class DbType:
    """Specifies the data type of a field, a property, or a Parameter object of a .NET data provider."""


class IsolationLevel:
    """Specifies the transaction locking behavior for the connection."""


class KeyRestrictionBehavior:
    """Identifies a list of connection string parameters identified by the KeyRestrictions property that are either allowed or not allowed."""


class LoadOption:
    """Controls how the values from the data source will be applied to existing rows when using the Load or Load method."""


class MappingType:
    """Specifies how a DataColumn is mapped."""


class MissingMappingAction:
    """Determines the action that occurs when a mapping is missing from a source table or a source column."""


class MissingSchemaAction:
    """Specifies the action to take when adding data to the DataSet and the required DataTable or DataColumn is missing."""


class ParameterDirection:
    """Specifies the type of a parameter within a query relative to the DataSet."""


class Rule:
    """Indicates the action that occurs when a ForeignKeyConstraint is enforced."""


class SchemaSerializationMode:
    """Indicates the schema serialization mode for a typed DataSet."""


class SchemaType:
    """Specifies how to handle existing schema mappings when performing a FillSchema(DataSet, SchemaType) operation."""


class SerializationFormat:
    """Determines the serialization format for a DataSet."""


class SqlDbType:
    """Specifies SQL Server-specific data type of a field, property, for use in a SqlParameter."""


class StatementType:
    """Specifies the type of SQL query to be used by the OleDbRowUpdatedEventArgs, OleDbRowUpdatingEventArgs, SqlRowUpdatedEventArgs, or SqlRowUpdatingEventArgs class."""


class UpdateRowSource:
    """Specifies how query command results are applied to the row being updated."""


class UpdateStatus:
    """Specifies the action to take with regard to the current and remaining rows during an Update(DataSet)."""


class XmlReadMode:
    """Specifies how to read XML data and a relational schema into a DataSet."""


class XmlWriteMode:
    """Specifies how to write XML data and a relational schema from a DataSet."""


# ---------- DELEGATES ---------- #

class DataColumnChangeEventHandler:
    """Represents the method that will handle the ColumnChanging event."""


class DataRowChangeEventHandler:
    """Represents the method that will handle the RowChanging, RowChanged, RowDeleting, and RowDeleted events of a DataTable."""


class DataTableClearEventHandler:
    """Represents the method that handles the Clear() method."""


class DataTableNewRowEventHandler:
    """Represents the method that handles the NewRow() method."""


class FillErrorEventHandler:
    """Represents the method that will handle the FillError event."""


class MergeFailedEventHandler:
    """Represents the method that will handle the MergeFailed event."""


class StateChangeEventHandler:
    """Represents the method that will handle the StateChange event."""


class StatementCompletedEventHandler:
    """The delegate type for the event handlers of the StatementCompleted event."""
