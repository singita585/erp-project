# import modules that we need in order to connect to mysql workbench
import pandas as pd
import mysql.connector as msql
from mysql.connector import Error

empdata = pd.read_csv('data.csv', index_col=False, delimiter = ',')
empdata.head()

# The purpose of this block of code is to create a database in mysql workbench
try:
    conn = msql.connect(host='localhost', user='root',
                        password='root')# Here you type in your username and password that you use when working with MySQL WorkBench
    if conn.is_connected():
        cursor = conn.cursor()
        cursor.execute('CREATE DATABASE customers')
        print('Database is created')
        cursor.execute(
except Error as e:
    print("Error while connecting to MySQL", e)


# The purpose of this block of code is to create a table
# And to insert the data that is in the csv file

try:
    conn = msql.connect(host='localhost', user='root', database='customers',
                        password='root')# Here you type in your username and password that you use when working with MySQL WorkBench
    if conn.is_connected():
        cursor = conn.cursor()
        cursor.execute("select database();")
        record = cursor.fetchone()
        print("You're connected to database: ", record)
        cursor.execute('DROP TABLE IF EXISTS employee_data;')
        print('Creating table....')
        # in the below line please pass the create table statement which you want #to create
        cursor.execute(
            "CREATE TABLE employee_data(first_name varchar(255),last_name varchar(255),birth varchar(255),month varchar(255),income int,expenses int")
        print("Table is created....")
        # loop through the data frame
        for i, row in empdata.iterrows():
            # here %S means string values
            sql = "INSERT INTO employee.customer_data VALUES (%s,%s,%s,%s,%s,%s)"
            cursor.execute(sql, tuple(row))
            print("Record inserted")
            # the connection is not auto committed by default, so we must commit to save our changes
            conn.commit()
except Error as e:
    print("Error while connecting to MySQL", e)



