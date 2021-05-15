# -*- coding: utf-8 -*-
"""
Created on Sat May 15 10:15:59 2021

@author: HP
"""

class ShowRecords:
    def accDetails(acc_No):
        import sqlite3
        conn=sqlite3.connect("bs1.db")
        c=conn.cursor()
        
        print(c.execute('''SELECT * FROM accounts 
                        WHERE acc_No = acc_No;''').fetchall())
        
    def transHist(acc_No):
        import sqlite3
        conn=sqlite3.connect("bs1.db")
        c=conn.cursor()
        
        print(c.execute('''SELECT * FROM transactions 
                        WHERE acc_No = acc_No;''').fetch
