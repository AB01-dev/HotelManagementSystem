import mysql.connector as sq
from random import randint
from customers import *
from insert import *
from delete import *
from read import read
from update import update


def connector():
    connection = sq.connect(host='localhost', database='hotel_management_system',
                              user='root', password='password')
    if connection.is_connected():
        pass
    return connection


def employees():
    print()
    print("Which operation do you wanna perform? ")
    print("""
            1 -----> Create Records
            2 -----> Read Records
            3 -----> Update  Records
            4 -----> Delete Records
            0 -----> Exit
""")
    Operation = input("Enter your choice: ")
    if Operation == '1':
        insert()
    elif Operation == '2':
        read()
    elif Operation == '3':
        update()
    elif Operation == '4':
        delete()
    elif Operation == '0':
        quit()
    else:
        print("Enter a valid option")
        e_update

    redo = input("Do you wish to perform another task (y/n)? ")
    if redo == 'y':
        employees()
    else:
        quit()


def cust_login():
    connection=connector()
    cursor=connection.cursor()
    C_ID = input("Enter your Customer ID: ")
    pswrd = input("Enter your password: ")
    cursor.execute(f"SELECT * from cust_login where C_ID = '{C_ID}' and password = '{pswrd}';")
    data=cursor.fetchall()
    count=cursor.rowcount
    if count>0:
        for row in data:
            print()
            print('Namaste', C_ID)
            customers()
    else:
        print()
        print("No record found")
        print()
        reg = input('Do you want to try again(y/n)? ')
        if reg == 'y':
            cust_login()
        else:
            quit()
    connection.close()

def emp_login():
    connection=connector()
    cursor=connection.cursor()
    username = input("Enter your username: ")
    pswrd = input("Enter your password: ")
    cursor.execute("SELECT * from emp_login where username = '{}' and password = '{}';" .format(username,pswrd))
    data=cursor.fetchall()
    count=cursor.rowcount
    if count>0:
        for row in data:
            print('You have successfuly logged in.')
            employees()
    else:
        print("No record found")
        emp_login()
    connection.close()

def cl_insert():
    cust_name = input("Enter your name: ")
    password = input("Enter a password for your profile: ")
    numb = randint(1000, 9999)
    C_ID = f"{cust_name[0]+cust_name[-1]}#{numb}"
    connection=connector()
    cursor=connection.cursor()
    cursor.execute(f"insert into cust_login values('{C_ID}', '{password}')")
    print('Congratulations! You are registered.')
    print(f"Your Customer ID is {C_ID}")
    connection.commit() 
    connection.close()
    cust_login()
