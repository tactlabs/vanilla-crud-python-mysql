'''
Created on Apr 20, 2017

@author: raja

source:
    https://www.w3schools.com/python/python_mysql_insert.asp
'''

#!/usr/bin/python
import base64;
import sys
import codecs
import MySQLdb;

db = MySQLdb.connect(host="localhost",    # your host, usually localhost
                     user="test",         # your username
                     passwd="test",  # your password
                     db="test")        # name of the data base

# you must create a Cursor object. It will let
#  you execute all the queries you need
cur = db.cursor()

# Use all the SQL you like
cur.execute("SELECT * FROM city")

# print all the first cell of all the rows
counter = 0;
for row in cur.fetchall():
    try:
        counter = counter + 1
        
        id = str(row[0])
        name = str(row[1])
        state = str(row[2])
        country = str(row[3])
        
        print(id + " - " +  name + " - " + state + " - "+country)
    except ValueError as e:
        print('Error')

db.close()