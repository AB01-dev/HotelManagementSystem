from login import *


def login():
    Select = input("Enter your choice: ")
    if Select == '1':
        print()
        print("               Welcome to Customer login           ")
        print("               1. login      2. Register           ")
        print()
        Option = input('Login or Register? ')
        if Option == '1':
            cust_login()
        elif Option == '2':
            cl_insert()
        else:
            print()
            print('Please select a Valid option.')
    elif Select == '2':
        print()
        print('         Welcome to Staff Quota          ')
        emp_login()
    else:
        print()
        print('Please select a Valid option.')


print("                 Ramagya School Noida                   ")
print("                Hotel Management System                 ")

print()
print('         Login/Register now to book a room           ')
print('         1. Customer              2. Staff           ')
print()
login()
print()
