# Quickstart

> :warning: **Warning!**
>
>  **This Quickstart tutorial is only for sqlite databases**

### Step One

Before you can do much of anything, you need to install and import SSQLA.

To install you can use `pip install SSQLA` 

Next you can import setup using `from SimpleAlchemy.sqliteS import setup`

### Step Two

Once you've made a database file you can use `engine_name = setup("{example_db_file}")` to setup an engine. `{example_db_file}` is the database file name, and `engine_name` can be whatever you want.

> :grey_exclamation: **Important**
> 
> Make sure to remember the engine name, as it is used often through out SSQLA

### Step 3

The complete program would be:
```
from SimpleAlchemy.sqliteS import setup

example_db_file = "{fileName}.db"

engine_name = setup(example_db_file)
```

### The Next Step?

Normally the next step would be to set up tables and columns



