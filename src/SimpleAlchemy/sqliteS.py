from sqlalchemy import create_engine, text, Table, MetaData, Column, Integer, String, UniqueConstrait
import string as s

def colData(colName, datatype, unique, nullable, PKey):
	data = None
	if datatype.lower() == "integer":
		if unique == True:
			if nullable == True:
				if PKey == True:
					data = Column(colName, Integer, unique=True, nullalbe=True, primary_key=True)
				elif PKey == False:
					data = Column(colName, Integer, unique=True, nullable=True)
			elif nullable == False:
				if PKey == True:
					data = Column(colName, Integer, unique=True, nullable=False, primary_key=True)
				elif PKey == False:
					data = Column(colName, Integer, unique=True, nullable=False)
		elif nullable == True and unique == False:
			if PKey == True:
				data = Column(colName, Integer, nullable=True, PKey=True)
			elif PKey == False:
				data = Column(colName, Integer, nullable=True)
			elif PKey == True and unique == False and nullable == False:
				data = Column(colName, Integer, nullable=False, primary_key=True)
			elif PKey == False and unique == False and nullable == False:
				data = Column(colName, Integer, nullable=False)
  return data
	
def setup(path: str, **extras):
  """Used to make an engine and a connection 

    Path: The file path used to make the connection
    for relative paths, don't use a / at the beginning, but for absolute paths, make sure to use a / at the beginning
    if you wish to use sqlite's :memory: identifier, leave path empty


		extras: Extras is a kwarg, and you can pass:
			Echo: Sets the echo setting for the SQLAlchemy Engine to whatever you pass it to be. Defaults to False

		-----
	
    Returns a SQLAlchemy Engine Instance
    """ 
	if "echo" in extras.keys():
		if extras['echo'] == True:
			echo = True
		elif extras['echo'] == False:
			echo = False
	elif "echo" not in extras.keys():
		echo = False
  if path.startswith('sqlite://'):
    raise ValueError(
      "That's how you would normally setup a connection to sqlite, but I've got it covered from this end!"
    )  # Throws an error if the user has the path include 'sqlite:///'
  elif path is None:
    e = create_engine("sqlite://", echo=echo)
  else:
    e = create_engine("sqlite:///" + path, echo=echo)
  return e


class SQL:
  """ This is a class that is used to complete SQL statements

        Methods:
        createColumn

        Attributes:
        None
    """

  @staticmethod
  def createColumn(columnName: str, datatype: str, **options):
    """ Used as a way to streamline the making of a column, but is entirely optional, if you know how to build it yourself

            ----------

            columnName: Column name is a required field, which is what will be used when trying to call for it in SQL statements

            datatype: Data type is optional, and is literally just what type it is, defaults to Integer

            options: options is an optional field, where you can pass things like unique and not null.
                     You can pass:
                         unique: adds the UNIQUE statement to the column
                         nullable: adds the NOT NULL statement if False
                         primarykey: adds the PRIMARY KEY statement
                     if none are passed, they will all default to false

                     they must be passed as strings or an error will be thrown

                     Please remember that in a table, there needs to be at least one column with a primary key

                     Foreign Keys, check, default, and index are not currently supported. They will be in the future

            ----------

            Returns a dictionary of strings and booleans
        """
		if columnName == "":
			raise ValueError("columnName can't be empty")
		else:
			Unique = False
			Nullable = False
			PrimaryKey = False
			if "unique" in options.keys():
				if options['unique'] == False:
					Unique = False
				elif options['unique'] == True:
					Unique = True
			else:
				Unique = False
			if "nullable" in options.keys():
				if options['nullable'] == False:
					Nullable = False
				elif options['nullable'] == True:
					Nullable = True
			elif "nullable" not in options.keys():
				Nullable = False
			if "primarykey" in options.keys():
				if options['primarykey'] == False:
					PrimaryKey = False
				elif options['primarykey'] == True:
					PrimaryKey = True
			elif "primarykey" not in options.keys():
				PrimaryKey = False
		data = colData(columnName, datatype, unique=Unique, nullable=Nullable, PKey=PrimaryKey)
		return data


  def createTable(table: str, columns: list, engine):
    """ Used to create a table for you

					-----------

					table: Table is a string used to make the table, AND it is the name of the table, make sure to remember it!



					columns: Columns is a list, that is composed of multiple dictionaries. These nested dictionaries contain data about creating each individual column. You can use the SQL.createColumns() method to make the process easier


          engine: Engine is a SQLAlchemy Engine instance. You can use the setup() function to get the instance


					-----------

					Returns nothing
			"""
    dictionary = {}
    alreadyPKey = False
    if table == "" or table is None:  # Testing if table is empty
      raise ValueError(
        "Table is empty, you must provide a table name. All you have to provide is a string"
      )  # If table is empty, throw an error saying that it is empty
    elif type(table) != type("string"):
      raise TypeError("Parameter 'table' is supposed to be a string")
    elif columns is None:
      raise ValueError(
        "The columns parameter is empty. It is a dictionary made of dictionaries, containing the data needed to create a column. You can use SQL.createColumns() to help create the columns. Remember, each time you call it, the function only makes ONE column, so you will need to repeat it to get the desired number of columns"
      )
    elif type(columns) != type(list()):
      raise TypeError("Parameter 'columns' is meant to be a list")
    elif table is not None:
      tableSQL = f"CREATE TABLE IF NOT EXISTS {table} ("
      for dict in columns:
        if type(dict) != type(dictionary):
          raise TypeError(
            "Parameter 'columns' is meant to be a dictionary made of dictionaries, with each dictionary containing data that details how a column is made"
          )
        dictName = dict['columnName']
        dictDataType = dict['dataType']
        if dict['unique'] is True:  # Checking if the Unique property is true
          dictUnique = True
        else:
          dictUnique = False

        if dict[
            'notnull'] is True:  # checking if the Not Null property is true
          dictNotNull = True
        else:
          dictNotNull = False

        if dict[
            'primarykey'] is True:  # checking if the Primary Key property is true
          dictPrimaryKey = True
        else:
          dictPrimaryKey = False

        if dictUnique is True:
          sqlUnique = " UNIQUE"
        else:
          sqlUnique = ""
        if dictNotNull is True:
          sqlNotNull = " NOT NULL"
        else:
          sqlNotNull = ""
        if alreadyPKey is False:
          if dictPrimaryKey is True:
            sqlPrimaryKey = " PRIMARY KEY"
            alreadyPKey = True
          else:
            sqlPrimaryKey = ""

        elif alreadyPKey is True and dictPrimaryKey is False:
          raise RuntimeError(
            "It appears that you have set multiple columns to be primary keys, and SQL does not allow for multiple primary keys. I suggest you change the settings of the column you don't want to be the primary key"
          )

        columnSql = f"{dictName} {dictDataType}{sqlUnique}{sqlNotNull}{sqlPrimaryKey},"
        tableSQL += columnSql  # Add the column data to the table data

      
      newTableSQL = tableSQL.rstrip(',') + ');'

    conn = engine.connect()
    conn.execute(text(newTableSQL))
    conn.commit()
    conn.close()
    
  def dropTable(table: str, engine):
    """
    ----------
    
    Drops a table from a SQLite Database

		----------

		WARNING! THIS IS AN IRREVERSIBLE ACTION! You will lose all data on the table, and the table itself

		----------

		table: The name of the table that you want to drop. Must be a string, or you will recieve an error.

 		engine: Engine is a SQLAlchemy Engine. You can create one using the setup() function

		----------

 		Returns nothing, except for sadness for the lost table
		"""
    
    
    if table == "":
      raise ValueError("table can't be an empty string. Use a table name that you have setup")
    meta = MetaData()
    Table(table, meta, autoload_with=engine).drop(engine)
      
