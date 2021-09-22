import pandas as pd
import mysql.connector as msql
from mysql.connector import Error
df = pd.read_csv (r'C:\Users\USER\Desktop\products.csv')   
df.head(10000000)

try:
    conn = msql.connect(host='localhost', user='root',  
                        password='')
    if conn.is_connected():
        cursor = conn.cursor()
        cursor.execute("CREATE DATABASE TestDB")
        print("TestDB database is created")
except Error as e:
    print("Error while connecting to MySQL", e)


try:
    conn = msql.connect(host='localhost', 
                           database='TestDB', user='root', 
                           password='')
    if conn.is_connected():
        cursor = conn.cursor()
        cursor.execute("select database();")
        record = cursor.fetchone()
        print("You're connected to database: ", record)
        print('Creating table....')
        cursor.execute("CREATE TABLE product (name text , sku text ,description text)")
        print("product table is created....")
        for i,row in df.iterrows():
            sql = "INSERT INTO Testdb.product VALUES (%s,%s,%s)"
            cursor.execute(sql, tuple(row))
            print("Record inserted")
            # the connection is not autocommitted by default, so we must commit to save our changes
            conn.commit()
except Error as e:
    print("Error while connecting to MySQL", e)
