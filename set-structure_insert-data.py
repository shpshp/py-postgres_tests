#!/usr/bin/python3
# -*- coding: utf-8 -*-
 
import psycopg2
import sys
 
 
con = None
 
try:
    con = psycopg2.connect("host='localhost' dbname='testdb' user='user' password='1'")   
    cur = con.cursor()
    #cur.execute("CREATE TABLE Products(Id serial PRIMARY KEY, Name VARCHAR(20), Price INT)")
    cur.execute("CREATE TABLE Products(Id serial PRIMARY KEY, Name VARCHAR(20), Price INT, Comment TEXT)")
    cur.execute("INSERT INTO Products (Name, Price, Comment) VALUES ('Milk', 5, 'This is a sample comment of a variable length. Lets check if theres a full thext search here')")
    cur.execute("INSERT INTO Products (Name, Price, Comment) VALUES ('Sugar', 7, 'This is another comment of a variable length. Lets check if theres a full thext search here')")
    cur.execute("INSERT INTO Products (Name, Price, Comment) VALUES ('Coffee', 3, 'This is a third comment of a variable length. Lets check if theres a full thext search here')")
    cur.execute("INSERT INTO Products (Name, Price, Comment) VALUES ('Bread', 5, 'Comment')")
    cur.execute("INSERT INTO Products (Name, Price, Comment) VALUES ('Oranges', 3, 'Comment')")
    con.commit()
except psycopg2.DatabaseError, e:
    if con:
        con.rollback()
 
    print 'Error %s' % e    
    sys.exit(1)
 
finally:   
    if con:
        con.close()

