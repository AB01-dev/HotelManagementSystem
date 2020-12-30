import mysql.connector as sq
import pandas as pd


def r_update():
    
    print("""
            1 -----> Room Status 
            2 -----> Room Charge 
            0 -----> Exit
""")
    table_name = input("Enter: ")
    if table_name == "1":
        r_RoomStatus()
    elif table_name == "2":
        r_RoomCharges()
    elif table_name == '0':
        quit()
    else:
        print("Enter a valid option")
        r_update()


def connector():
    connection=sq.connect(host='localhost', database='hotel_management_system', user='root', password='password')
    if connection.is_connected():
        pass
    return connection

def r_read():
    connection = connector()
    print("         We have the following rooms for you         ")
    df = pd.read_sql("SELECT room_no, room_type, room_charges FROM rooms where room_status = 'Available'", connection)
    print()    
    print(df)
    print()
    connection.close()

def r_insert():
     connection = connector()
     Floor_no = input("Enter floor no: ")
     Room_no = input("Enter room no: ")
     Room_Status = input("Enter room status: ")
     Room_Charges = input("Enter room charge(per night): ")
     
     cursor=connection.cursor()
     cursor.execute("insert into rooms values({}, {}, '{}', '{}')" 
                    .format(Floor_no, Room_no, Room_Status, Room_Charges))
     connection.commit()
     connection.close()

def r_RoomCharges():
    connection = connector()
    Room_Charges = input("Enter Updated room charges: ")
    Room_no = input("Enter room no: ")
    
    cursor=connection.cursor()
    cursor.execute("update Rooms set Room_Charges = {} where Room_no = {}"
                   .format(Room_Charges, Room_no))
    connection.commit()
    print()
    print("Updated")
    print()
    connection.close()

def r_RoomStatus():
    connection = connector()
    Room_Status = input("Enter Updated room status: ")
    Room_no = input("Enter room no: ")

    cursor=connection.cursor()
    cursor.execute("update Rooms set Room_Status = '{}' where Room_no = {}"
                   .format(Room_Status, Room_no))
    connection.commit()
    print("Updated")
    connection.close()
