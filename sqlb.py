# using INSERT command

import sqlite3

# create the connection object
conn = sqlite3.connect("new.db")

# get a cursor object used to execute SQL commands
cursor = conn.cursor()

# insert data
cursor.execute("INSERT INTO population VALUES('New York City', \
    'NY', 8200000)")
cursor.execute("INSERT INTO population VALUES('San Francisco', \
    'CA', 800000)")

# commit the changes
conn.commit()

# close the database connection
conn.close()

# now instead do some inserts connecting with the 'with' keyword (doen't need a commit)
with sqlite3.connect("new.db") as connection:
    c = connection.cursor()
    c.execute("INSERT INTO population VALUES('Cleveland', 'OH', 390000)")

# believe the 'with' block doesn't close the connection
connection.close()

