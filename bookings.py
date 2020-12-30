import mysql.connector as sq
import pandas as pd


def b_update():
    print("""
            1 -----> Departure 
            2 -----> Room Charge  
            3 -----> Total Stay
            4 -----> Total Pay
            0 -----> Exit
""")
    table_name = input("Enter: ")
    if table_name == "1":
        b_Departure()
    elif table_name == "2":
        b_RoomCharge()
    elif table_name == "3":
        b_TotalStay()
    elif table_name == '4':
        b_TotalPay()
    elif table_name == '0':
        quit()
    else:
        print("Please enter a valid option")
        b_update()

def connector():
    connection = sq.connect(host='localhost',
                          database='hotel_management_system',
                          user='root',
                          password='password')
    if connection.is_connected():
        pass
    return connection


def b_Departure(): 
    connection = connector()
    Departure = input("Enter Updated departure date: ")
    Adhar_no = input("Enter adhar no: ")
    cursor=connection.cursor()
    cursor.execute("update Bookings set Departure = '{}' where Adhar_no = {} "
                       .format(Departure, Adhar_no))
    connection.commit()
    print()
    print("Succesfully Updated")
    print()
    connection.close()
    
def b_insert():
    connection = connector()
    C_ID = input("Enter your Customer ID: ")
    Cust_Name = input("Enter name: ")
    Adhar_no = input("Enter adhar no: ")
    Room_no = input("Enter room no: ")
    Arrival = input("Enter date of arrival: ")
    Departure = input("Enter date of departure: ")
    Room_Charge = int(input("Enter the base room charge: "))
    Total_Stay = int(input("Enter no of days spent: "))
    Total_Pay = Room_Charge * Total_Stay
    cursor=connection.cursor()
    cursor.execute("insert into bookings values('{}','{}',{}, {}, '{}', '{}', {}, {}, {}, 'IN')" 
                   .format(C_ID, Cust_Name, Adhar_no, Room_no, Arrival, Departure, Room_Charge, Total_Stay, Total_Pay, Status))
    connection.commit()
    connection.close()
    
def b_read():
    connection = connector()
    df = pd.read_sql("SELECT * FROM Bookings", connection)
    print()
    print(df)
    print()
    connection.close()
    
def b_RoomCharge():
    connection = connector()
    Room_Charge = input("Enter Updated room charge: ")
    Adhar_no = input("Enter adhar no: ")
    cursor=connection.cursor()
    cursor.execute("update Bookings set Room_Charge = {} where Adhar_no = {} "
                       .format(Room_Charge, Adhar_no))
    connection.commit()
    print()
    print("Updated")
    print()
    connection.close()

def b_TotalPay():
    connection = connector()
    Total_Pay = input("Enter Updated total pay: ")
    Adhar_no = input("Enter adhar no: ")
    cursor=connection.cursor()
    cursor.execute("update Bookings set Total_Pay = {} where Adhar_no = {} "
                       .format(Total_Pay, Adhar_no))
    connection.commit()
    print()
    print("Updated")
    print()
    connection.close()
    
def b_TotalStay():
    connection = connector()
    Total_Stay = input("Enter Updated total stay: ")
    Adhar_no = input("Enter adhar no: ")
    cursor=connection.cursor()
    cursor.execute("update Bookings set Total_Stay = {} where Adhar_no = {} "
                       .format(Total_Stay, Adhar_no))
    connection.commit()
    print()
    print("Updated")
    print()
    connection.close()
