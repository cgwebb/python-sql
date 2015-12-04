# import from CSV

import csv
import sqlite3

with sqlite3.connect("new.db") as connection:
    c = connection.cursor()
    
    # open the csv file and assign it to a variable; 'U' is universal newline mode
    employees = csv.reader(open("employees.csv", "rU"))
    
    # create a new table called 'employees'
    c.execute("CREATE TABLE employees(firstname TEXT, lastname TEXT)")
    
    # insert data into table; note the use of the form that specifies the column names
    c.executemany("INSERT INTO employees(firstname, lastname) VALUES (?, ?)", employees)

connection.close()
