import mysql.connector as sq
from bookings import b_insert
from customers import c_insert
from employees import e_insert
from rooms import r_insert


def insert():
    print("""
            1 -----> bookings
            2 -----> customers
            3 -----> employees
            4 -----> Rooms
            0 -----> Exit
""")
    print()
    table_name = input("Select in which table you want to add a record: ")
    if table_name == "1":
        b_insert ()
    if table_name == "2":
        c_insert()
    if table_name == "3":
        e_insert()
    if table_name == "4":
        r_insert()
    elif table_name == '0':
        quit()
