from sqlalchemy import create_engine, connect. text
import string as s

def setup(Optional[path]: string):
    """ Used to make an engine and a connection 


        Path: The file path used to make the connection
        for relative paths, don't use a / at the beginning, but for absolute paths, make sure to use a / at the beginning
				if you wish to use sqlite's :memory: identifier, leave path empty

        Returns a Dictionary containing:
				An SQLAlchemy Engine instance named engine, and
				A SQLAlchemy Connection instance named connection
    """
		if path.startswith("sqlite:///", 0):
			raise ValueError("That's how you would normally setup a connection to sqlite, but I've got it covered from this end!") # Throws an error if the user has the path include 'sqlite:///' 
		elif:
			e = create_engine("sqlite://")
			conn = e.connect()
			dict = {"engine": e, "connection": conn}
			return dict
		else:
    	e = create_engine(f"sqlite:///{path}")
			conn = e.connect()
			dict = {"engine": e, "connection": conn}
			return dict


class SQL:
		""" This is a class that is used to complete SQL statements

 				Methods:
		 		createTable 
		 		createColumn

	 			Attributes:
				None
		"""
		def createColumn(columnName: string, datatype[optional]: string, **options):
			""" Used as a way to stream line making a column, but is entirely optional, if you know how to build it yourself

					----------
	
	 				columnName: Column name is a required field, which is what will be used when trying to call for it in SQL statements		



		 			datatype: Data type is optional, and is literally just what type it is, defaults to NUMERIC



	 				options: options is a optional field, where you can pass things like unique and not null.
					You can pass:
		 				unique: adds the UNIQUE statement to the column
			 			NotNull: adds the NOT NULL statement
			 			PrimaryKey: adds the PRIMARY KEY statement, and if passed, unique or NotNull will automatically be considered true
			 		if none are passed, they will all default to false

	 				they must be passed as strings or an error will be thrown
			
					Please remember that in a table, there needs to be at least one column with a primary key
		 
			 		Foreign Keys, check, default, and index are not currently supported. They will be in the future

					----------

	 				Returns a dictionary of strings and booleans
	 		"""

			columnData = {
				"columnName": "",
				"datatype": "",
				"unique": False,
				"notnull": False,
				"primarykey": False
}

			if columnName is None:
				raise ValueError("columnName can't be empty, it must be a string")
			elif columnName is not None:
				columnData['columnName'] = columnName
				
				if datatype is None:
					datatype = "NUMERIC"

					columnData['dataType'] = datatype.upper()
				elif datatype.upper() != "TEXT" or "NUMERIC" or "INTEGER" or "REAL" or "NONE":
					raise ValueError("datatype must be one of the allowed data types for sqlite, which includes, text, numeric, integer, real, or none. I would suggest visiting https://geeksforgeeks.org/sqlite-data-types if you don't know what those options mean"
				
				else:
					columnData['dataType'] = datatype.upper()
					
				if len(options) > 0: # checks if any kwargs were passed
					if len(options) < 4: # checks if the number of kwargs passed is less than 4
						for x in options.values():
							if x.lower() == "unique" or "notnull" or "primarykey": # checks if the kwargs passed are actually the allowed kwargs
								if x.lower() == "unique":
									columnData['unique'] = True
								if x.lower() == "notnull":
									columnData['notnull'] = True
								if x.lower() == "primarykey":
									columnData['primarykey'] = True
									columnData['unique'] = True
									columnData['notnull'] = True

								return columnData
							else:		
								raise ValueError(f"The kwarg {x} you sent isn't allowed, you can only send unique, notnull, or primarykey. Don't worry, they are case-insensitive")
								
					else:
						raise ValueError("Their isn't more than three passable kwargs, unique, notnull, or primarykey. Any more than three kwargs, and I won't know what to do with the rest")
				else:
					return columnData
					
			
	
		def createTable(table: string, unique[optional]: boolean = True,):
			""" Used to create a table for you

					-----------

					table: Table is a string used to make the table, AND it is the name of the table, make sure to remember it!



		 			unique: Unique is basically asking if you want the SQL statement "IF NOT EXISTS" to be used in making the table, defaults to true


					-----------

					Returns nothing
			"""
			if table is None: # Testing if table is empty
				raise ValueError("Table is empty, you must provide a table name. All you have to provide is a string") # If table is empty, throw an error saying that it is empty
			elif table is not None: 
				if unique is None:
					unique = True
				if unique is True:
					sql = f"IF NOT EXISTS CREATE TABLE {table}"









					
