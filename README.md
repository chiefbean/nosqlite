# NoSQLite

A JSON based flat file NoSQL database.

## Usage

```python
from nosqlite.nosqlite import NoSQLite

ns = NoSQLite('file.json')

# Create a new table
ns.create_table('users')

# Insert a new record into the table
ns.insert({'username':'blah', 'password':'blah'}, 'users')

# Find a record in a table
ns.find({'username':'blah'}, 'users')

# Update a record in a table
ns.update({'username':'blah'}, {'username':'changed', 'password':'changed'}, 'users')

# Delete a record from a table
ns.delete({'username':'blah', 'password':'blah'}, 'users')
```

## Documentation

```python
# filename: name of local file/path to json data file
class NoSQLite(filename)
  
  # reload the json file (used by the class to update the jsonData after writing)
  reload()
  
  # write json data to file and reload
  writeOut()
  
  # creates a new table in the json data
  # tableName: name of table to be created
  create_table(tableName)
  
  # inserts data into table
  # data: json data to be inserted
  # table: name of table to insert into
  insert(data, table)
  
  # deletes data from table, deletes first found
  # data: json data to search table for
  # table: table to search and delete from
  delete(data, table)

  # deletes data from table, deletes all found
  # data: json data to search table for
  # table: table to search and delete from
  deleteMany(data, table)
  
  # updates data in table with newData, updates first found
  # data: json data to search table for
  # newData: new json data to change record to
  # table: table to search and update from
  update(data, newData, table)

  # updates data in table with newData, updates all found
  # data: json data to search table for
  # newData: new json data to change record to
  # table: table to search and update from
  updateMany(data, newData, table)

  # find all data in table
  # table: table to search
  findAll(table)

  # find data in table, returns all matching records
  # data: json data to search table for
  # table: table to search
  find(data, table)

  # find data in table, returns first matching record
  # data: json data to search table for
  # table: table to search
  findOne(data, table)
```
