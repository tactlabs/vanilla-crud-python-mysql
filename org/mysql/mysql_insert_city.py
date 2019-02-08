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


def get_db():

    db = MySQLdb.connect(host="localhost",    # your host, usually localhost
                     user="ani",         # your username
                     passwd="ani",  # your password
                     db="test")        # name of the data base
    
    return db

def insert_city(db, name, city, country):
    
    # you must create a Cursor object. It will let
    #  you execute all the queries you need
    cur = db.cursor()
    
    #
    sql = "INSERT INTO CITY (NAME, STATE, COUNTRY) VALUES (%s, %s, %s)"
    values = (name, city, country)

    # Use all the SQL you like
    cur.execute(sql, values)

    db.commit()

    print('Done : '+str(cur.rowcount)+" inserted")
    

def main():
    
    db = get_db();
    
    insert_city(db, 'Cuddalore', 'TA', 'India')
    insert_city(db, 'Kumbakonam', 'TA', 'India')
    
    db.close()

if __name__ == '__main__':
    main()
    
