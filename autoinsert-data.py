#!/usr/bin/python3
# -*- coding: utf-8 -*-
 
import psycopg2
import sys
import time
import datetime

con = None

try:
    con = psycopg2.connect("host='localhost' dbname='testdb' user='user' password='1'")   
    cur = con.cursor()
    counter = 0
    try:
        while True:
            for i in range(0,100):
                command = "INSERT INTO Products (Name, Price, Comment) VALUES ('Auto-genAuto-gen', " + str(i) + ", 'CommentCommentCommentCommentCommentCommentCommentCommentCommentCommentCommentCommentCommentCommentCommentCommentCommentCommentCommentComment')"
                cur.execute(command)
                con.commit()
                #print "added " + str(counter)
                counter = counter + 1
            #time.sleep(0.5)
            #print(datetime.now().strftime("%Y-%m-%d_%H-%M-%S"))
    except:
        print 'Interrupted'
except psycopg2.DatabaseError, e:
    if con:
        con.rollback()
 
    print 'Error %s' % e    
    sys.exit(1)
 
finally:   
    if con:
        con.close()

