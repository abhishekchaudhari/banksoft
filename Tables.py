# -*- coding: utf-8 -*-
"""
Created on Sat May 15 00:25:56 2021

@author: HP
"""
class CreateTables:
    #from flask import jsonify
    import sqlite3
    conn= sqlite3.connect("bs1.db")
    
    c=conn.cursor()
    
    c.execute("""CREATE TABLE customers(
            cust_ID NUMBER(5) PRIMARY KEY,
            cust_name VARCHAR2(40) ,
            cust_phone NUMBER(10),
            cust_login VARCHAR2(40),
            cust_password VARCHAR2(40), 
             cust_address VARCHAR2(40));
            """)
    
    c.execute("""CREATE TABLE accounts(
            acc_No NUMBER(5) PRIMARY KEY,
            acc_holder_name VARCHAR(40),
            acc_type VARCHAR2(20),
            acc_balance NUMBER(10),
            acc_branch NUMBER(10),
            cust_ID NUMBER(5) FOREIGN KEY REFERENCES customers(cust_ID),
            CONSTRAINT pk_acc PRIMARY KEY(acc_No,acc_branch)
            );            
            """)
    
    c.execute('''CREATE TABLE transactions(
            acc_No NUMBER(5) FOREIGN KEY REFERENCES accounts(acc_No),
            t_balance NUMBER(10),
            debit_amt NUMBER(10),
            credit_amt NUMBER(10));
                ''')
    
    
    c.execute("""
              INSERT INTO customers values(12345,
              'Abhi',
              8378000531,
              'a@gmail.com',
              'abhi')
              """)
              
    conn.close()

