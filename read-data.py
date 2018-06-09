#!/usr/bin/python3
# -*- coding: utf-8 -*-
 
import psycopg2
import sys
 
 
con = None
 
try:
    con = psycopg2.connect("host='localhost' dbname='testdb' user='user' password='1'")   
    cur = con.cursor()
    cur.execute("SELECT * FROM Products")
 
    while True:
        row = cur.fetchone()
 
        if row == None:
            break
 
        print("Id=" + str(row[0]) + "; Product=" + row[1] + "; Price=" + str(row[2]) + "; Comment=" + str(row[3]))
 
except psycopg2.DatabaseError, e:
    if con:
        con.rollback()
 
    print 'Error %s' % e    
    sys.exit(1)
 
finally:   
    if con:
        con.close()

