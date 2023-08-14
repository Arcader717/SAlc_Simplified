# **Creating Tables, columns, and even dropping some**
Based on the v0.4 update, "Creating Tables, Columns, and even dropping some"
***
If you don't have an engine setup, you should visit the [Quickstart](https://ssqla.readthedocs.io/en/latest/introduction/quickstart/) tutorial

# Importing the SQL class

The first step is to import the SQL class, using `from SimpleAlchemy.sqliteS import SQL`.
***
# Makiing the Columns

Next, you need to make a dictionary of the column, containing the data of how you want the column setup. 

While you could make a dictionary yourself, using `dictName = {"columnName": "", "columnDataType": "", "unique": False, "notnull": False, "primarykey": False}`, you could also use the `SQL.createColumn()` method.

Using the `SQL.createColumn()` method, you can define the column name and the data type of the column, so you could have a column named `columnName` and have the data type `numeric`.

To get that you would do `SQL.createColumn("columnName",  "numeric")` and use a variable to hold the dictionary

> **Warning!**
>
> Make sure not to have more than one column that has primary key set to true, or else it will throw an error when making the table
***
# Making The Table

After you make your columns, you can put them in a list and then put them into the `SQL.createTable()` method to make a table. `createTable()`'s syntax is `SQL.createTable(table: str, columns: list, engine)` where `table` is just the table name, and `columns` is the list that I told you about earlier, and `engine` is from the `setup()` function

## Extra!

If you create a table that you decide that you had messed up, or just want to flat-out delete it, you can use the `SQL` class method `dropTable()` to delete the table and all the data inside of it.

> **Warning!**
>
> Dropping a table means losing the table and all of its data, and it will be irreversible, so think carefully before deciding to drop a table

syntax: `SQL.dropTable(table: str)` with `table` being the table you want to drop

# Final Example
> **Note!**
>
> The engine comes from the quickstart tutorial listed at the top of this page or you can click [here](https://ssqla.readthedocs.io/en/latest/introduction/quickstart/) to visit the quickstart tutorial

using three columns, 
```
from SimpleAlchemy.sqliteS import setup, SQL

example_db_file = "{fileName].db"

engine = setup(example_db_file)

column1 = SQL.createColumn("column1", "numeric", unique=True, notnull=True, primarykey=True)
column2 = SQL.createColumn("column2", "numeric", unique=True)
column3 = SQL.createColumn("column3", "") # datatype defaults to numeric if empty

columnList = [column1, column2, column3]

SQL.createTable(tableName, columnList)
```

# The End

Sadly this is the end of the introduction, but it will be expanded after the v0.5 update! See you then!

