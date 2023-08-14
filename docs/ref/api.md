# SSQLA Reference
Here see full information on how to use the methods and functions in SSQLA
***
# SqliteS
Has the reference info about the SQLite version of SSQLA

## Setup
- `setup(file: path, **extras)`
  - Used to setup a SQLAlchemy Engine
  - Returns a SQLAlchemy Engine
  - Parameters:
    - File (path) - The file path to the database you want to use
    - extras (kwargs) - Passable:
      - echo (bool) - Whether you want every sql statement passed to be recorded into the console or not 
  - Raises:
    - [ValueError](https://docs.python.org/3/library/exceptions.html#ValueError) - the string "sqlite://" was passed. It errors out because the system already uses "sqlite://" combined with the path provided
***
- ## SQL
  - `class SimpleAlchemy.sqliteS.SQL()`
  - Methods:
    - `createColumn(columnName: str, datatype: str = "NUMERIC", **options)`
      - Used to create a variable that contains the needed data to use `createTable()`
      - Returns a dictionary containing information about how to set up a column for the `createTable()` method
      - Parameters:
        - columnName (str) - The name of the column. Will be used to call upon the column
        - datatype (str) - The datatype of the column. Accepts numeric, text, integer, real, and none. Visit [geeksforgeeks](https://geeksforgeeks.org/sqlite-data-types) if you don't know what the data types do
        - options (kwargs) - Passable:
          - unique (bool) - Whether to include the `UNIQUE` statement when defining the column. Defaults to `False`
          - notnull (bool) - Whether to include the `NOT NULL` statement when defining the column. Defaults to `False`
          - primarykey (bool) - Whether to include the `PRIMARY KEY` statement when defining the column. Defaults to `False`
      - Raises:
        - [ValueError](https://docs.python.org/3/library/exceptions.html#ValueError) - columnName can't be empty. Simple as that
        - [ValueError](https://docs.python.org/3/library/exceptions.html#ValueError) - datatype must be one of the SQLite datatypes. Visit [geeksforgeeks](https://geeksforgeeks.org/sqlite-data-types) to learn the accepted SQLite data types
        - [ValueError](https://docs.python.org/3/library/exceptions.html#ValueError) - The kwarg {option} you sent isn't included in the supported list of kwargs, which are: unique, notnull, or primarykey. Don't worry they are case-insensitive
       
    - `createTable(table: str, columns: list, engine)`
      - Used to create a table using the SQL `CREATE TABLE` statement
      - Returns nothing
      - Parameters:
        - table (string) - The name of the table. Used to call upon the table
        - columns (list) - A list of dictionaries, with full information on how to build each column
        - engine (SQLAlchemy.engine) - The engine used to complete SQL statements with SQLAlchemy. Refer to the [setup](https://ssqla.readthedocs.io/en/latest/ref/api
      - Raises:
        - [ValueError](https://docs.python.org/3/library/exceptions.html#ValueError) - table is empty, you must provide a table name
        - [RuntimeError](https://docs.python.org/3/library/exceptions.html#RuntimeError) - 
  
