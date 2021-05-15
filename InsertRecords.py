# -*- coding: utf-8 -*-
"""
Created on Sat May 15 09:39:44 2021

@author: HP
"""


class InsertRecords:
    import sqlite3
    conn=sqlite3.connect("bs1.db")
    c=conn.cursor()
    def InsertCust(c1=12345,c2='Abhi',
                   c3=8888899999,c4='abhirc',
                   c5='password',c6='Pune'):
#        import sqlite3
#        conn=sqlite3.connect("bs1.db")
#        c=conn.cursor()
        
        c.execute('''INSERT INTO customers VALUES(
                c1,c2,c3,c4,c5,C6);
                ''')
    def InsertAcc(ac1=12345,ac2='Abhi',ac3='Saving',
                  ac4=10000,ac5=111,ac6=12):
        c.execute('''INSERT INTO accounts VALUES(
                ac1,ac2,ac3,ac4,ac5,ac6);
                ''')
    def InsertTrans(t1,t2,t3,t4):
        c.execute('''INSERT INTO transactions VALUES(
                t1,t2,t3,t4);
                ''')
        
       