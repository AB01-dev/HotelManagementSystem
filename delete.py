import mysql.connector as sq
from customers import *
from employees import *


def delete():

    print("""
            1 -----> Customers
            2 -----> Employees
            0 -----> Exit
""")

    table_name = input("Enter table no.: ")
    if table_name == "1":
        c_del()
    if table_name == "2":
        e_del()
    elif table_name == '0':
        quit()
