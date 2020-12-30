import mysql.connector as sq
from bookings import *
from customers import *
from employees import *
from rooms import *

def update():
    print("""
            1 -----> Bookings 
            2 -----> Customers 
            3 -----> Employees  
            4 -----> Rooms
            0 -----> Exit
""")
    table_name = input("Enter which table you want to update: ")
    if table_name == "1":
        b_update()
    elif table_name == "2":
        c_update()
    elif table_name == "3":
        e_update()
    elif table_name == "4":
        r_update()
    elif table_name == '0':
        quit()
    else:
        print("Enter a valid option")
        update()
