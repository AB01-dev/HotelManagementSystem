import mysql.connector as sq
import pandas as pd
from bookings import b_read
from customers import c_read
from employees import e_read
from rooms import r_read

def connector():
    connection=sq.connect(host='localhost',
                            database='hotel_management_system',
                            user='root',
                            password='password')

    if connection.is_connected():
        pass
    return connection

def co_read():
    connection = connector()
    df = pd.read_sql("SELECT * FROM Checkouts", connection)
    print(df)
    connection.close()

def fe_read():
    connection = connector()

    df = pd.read_sql("SELECT * FROM former_emp", connection)

    print(df)

    connection.close

def read():
    print("""
            1 -----> Bookings 
            2 -----> Customers 
            3 -----> Checkouts 
            4 -----> Employees  
            5 -----> former_emp
            6 -----> Rooms
            0 -----> Exit
""")
    print()
    table_name = input("Which table you want to read: ")
    print()
    if table_name == "1":
        b_read()
    elif table_name == "2":
        c_read()
    elif table_name == "3":
        co_read()
    elif table_name == "4":
        e_read()
    elif table_name == "5":
        fe_read()
    elif table_name == "6":
        r_read()
    elif table_name == '0':
        quit()
    else:
        print("Enter a valid option")
        read()
