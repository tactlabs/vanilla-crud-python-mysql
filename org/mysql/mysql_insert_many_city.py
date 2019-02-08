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
                     user="ani",         # your username
                     passwd="ani",  # your password
                     db="test")        # name of the data base

# you must create a Cursor object. It will let
#  you execute all the queries you need
cur = db.cursor()

#
sql = "INSERT INTO CITY (NAME, STATE, COUNTRY) VALUES (%s, %s, %s)"
values = [
    ("Theni", "TA", "India"),
    ("Trichy", "TA", "India")
    ]

# Use all the SQL you like
cur.executemany(sql, values)

db.commit()

print('Done : '+str(cur.rowcount)+" inserted")

db.close()