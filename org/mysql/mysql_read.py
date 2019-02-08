'''
Created on Apr 20, 2017

@author: raja
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

# Use all the SQL you like
cur.execute("SELECT * FROM CITY")

# print all the first cell of all the rows
counter = 0;
for row in cur.fetchall():
    try:
        counter = counter + 1;
        title = str(row[2]);
        company = str(row[3]);
        print(str(counter) + " - " +  title + " - " + company);
    except ValueError as e:
        print('Error');

db.close()