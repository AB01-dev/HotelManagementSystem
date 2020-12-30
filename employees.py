import mysql.connector as sq
import pandas as pd


def connector():
    connection = sq.connect(host='localhost', database='hotel_management_system', user='root', password='password')
    if connection.is_connected():
        pass
    return connection


def e_del():
    connection = connector()        
    adhar_no = input("Enter adhar no: ")
    cursor=connection.cursor()
    cursor.execute("insert into former_emp select * from employees where adhar_no = {}"
                   .format(adhar_no))
    cursor.execute("delete from employees where adhar_no = {}".format(adhar_no))
    connection.commit()
    print()
    print("Successfully Removed the employee data from the employees table.")
    print()
    connection.close()

def e_Address():
    connection = connector()
    e_Address = input("Enter Updated Address: ")
    Adhar_no = input("Enter Adhar no: ")
    cursor=connection.cursor()
    cursor.execute("update Employees set e_Address = '{}' where Adhar_no = {}"
                   .format(e_Address, Adhar_no))
    connection.commit()
    print()
    print("Updated")
    print()
    connection.close()
    
def e_insert():
    connection = connector()
    e_name = input("Enter name: ")
    e_address = input("Enter address: ")
    Phone_no = input("Enter phone no: ")
    Adhar_no = input("Enter adhar no: ")
    Joining_Date = input("Enter Date: ")
    Position = input("Enter the postion: ")
    Salary = input("Enter the salary: ")
    cursor=connection.cursor()
    cursor.execute("insert into Employees values('{}','{}', {}, {}, '{}', '{}', {})"
                   .format(e_name, e_address, Phone_no, Adhar_no, Joining_Date, Position, Salary))
    connection.commit()
    connection.close()

def e_PhoneNo():
    connection = connector()
    Phone_No = input("Enter Updated phone no: ")
    Adhar_No = input("Enter adhar no: ")
    cursor=connection.cursor()
    cursor.execute("update Employees set Phone_No = {} where Adhar_No = {} "
                   .format(Phone_No, Adhar_No))
    connection.commit()
    print()
    print("Updated")
    print()
    connection.close()

def e_Position():
    connection = connector()
    e_position = input("Enter Updated position: ")
    Adhar_no = input("Enter adhar no: ")
    cursor=connection.cursor()
    cursor.execute("update Employees set position = '{}' where Adhar_no = {}"
                   .format(e_position, Adhar_no))
    connection.commit()
    print()
    print("Updated")
    print()
    connection.close()

def e_read():
    connection = connector()
    df_query = pd.read_sql("SELECT * FROM Employees", connection)
    print()
    print(df_query)
    print()
    connection.close()

def e_Salary():
    connection = connector()
    Salary = input("Enter the Updated salary: ")
    Adhar_no = input("Enter adhar no: ")
    cursor=connection.cursor()
    cursor.execute("update Employees set Salary = {} where Adhar_no = {}".format(Salary, Adhar_no))
    connection.commit()
    print()
    print("Updated")
    print()
    connection.close()

def e_update():
    
    print("""
            1 -----> Address
            2 -----> Phone No 
            3 -----> Position 
            4 -----> Salary
            0 -----> Exit
""")
    
    table_name = input("Enter what you want to update: ")
    if table_name == "1":
        e_Address()
    elif table_name == "2":
        e_PhoneNo()
    elif table_name == "3":
        e_Position()
    elif table_name == "4":
        e_Salary()
    elif table_name == '0':
        quit()
    else:
        print("Enter a valid option")
        e_update()
