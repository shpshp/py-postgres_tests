#!/usr/bin/python3
# -*- coding: utf-8 -*-
 
import psycopg2
import sys
 
 
con = None
 
try:
    con = psycopg2.connect("host='localhost' dbname='testdb' user='pythonspot' password='1'")   
    cur = con.cursor()
    cur.execute("UPDATE Products SET Price=%s WHERE Id=%s", (10, 4))      
    con.commit()
except psycopg2.DatabaseError, e:
    if con:
        con.rollback()
 
    print 'Error %s' % e    
    sys.exit(1)
 
finally:   
    if con:
        con.close()

