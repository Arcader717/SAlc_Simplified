from sqlalchemy import create_engine, connect
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
		if path.startswith("sqlite:///", 0)
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
