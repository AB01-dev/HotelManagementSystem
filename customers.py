import mysql.connector as sq
import pandas as pd
import datetime
from rooms import *

def connector():    
    connection = sq.connect(host='localhost',
                            database='hotel_management_system',
                            user='root',
                            password='password')
    if connection.is_connected():
         pass
    return connection

def cust_read():
    connection = connector()
    C_ID = input("Enter your Customer ID: ")
    df = pd.read_sql(f"SELECT * FROM Bookings WHERE C_ID = '{C_ID}'", connection)
    print()
    print(df)
    print()
    connection.close()
         
def c_del():
    connection = connector()
    Room_no = input("Enter room no: ")
    
    Arrival = pd.read_sql(f"SELECT Entry_Date FROM Customers where room_no = {Room_no}", connection)
    Arrival = Arrival.iloc[0,0]
    Arrival = str(Arrival)
    Arrival_Date = int(Arrival[8] + Arrival[9])
    Arrival_Mnth = int(Arrival[5] + Arrival[6])
    Arrival_Year = int(Arrival[0] + Arrival[1] + Arrival[2] + Arrival[3])
    Departure = datetime.date.today().isoformat()
    Departure_Date = int(Departure[8] + Departure[9])
    Departure_Mnth = int(Departure[5] + Departure[6])
    Departure_Year = int(Departure[0] + Departure[1] + Departure[2] + Departure[3])
    
    Room_charge = pd.read_sql(f"SELECT room_charges FROM rooms where room_no = {Room_no}", connection)
    Room_charge = Room_charge.iloc[0,0]
    
    Total_Stay = abs(datetime.date(Departure_Year, Departure_Mnth, Departure_Date) - datetime.date(Arrival_Year, Arrival_Mnth, Arrival_Date))
    Total_Stay = Total_Stay.days
    Total_Pay = int(Total_Stay) * Room_charge
    
    cursor=connection.cursor()
    cursor.execute(f"INSERT INTO CheckOuts SELECT * FROM Customers WHERE Room_no = {Room_no}")
    cursor.execute(f"UPDATE Rooms SET Room_Status = 'Available' where Room_no = {Room_no}")
    cursor.execute(f"UPDATE Bookings SET Departure = '{Departure}', Status = 'Out', Total_Stay = {Total_Stay}, Total_Pay = {Total_Pay} WHERE Room_no = {Room_no}")
    cursor.execute(f"DELETE FROM Customers WHERE Room_no = {Room_no}")
    df = pd.read_sql(f"SELECT * FROM Bookings WHERE Room_no = {Room_no} AND Departure = '{Departure}' AND Total_Pay = {Total_Pay}", connection)
    Arrived = df.iloc[0,4]
    Departured = df.iloc[0,5]
    Total_Stayed = df.iloc[0,7]
    Room_Charges = df.iloc[0,6]
    Total_Amount = df.iloc[0,8]
    print(f"""
|───────────────────────────────────────────────────────────────────|
                                                                      
                Arrived at:                 {Arrived}               
                Deparure at:                {Departured}             
                No. of days stayed:         {Total_Stayed}           
                Room Charge (per day):      {Room_Charges}           
                                                                     
|───────────────────────────────────────────────────────────────────|                                                                   
                Total Payout:               {Total_Amount}          
|───────────────────────────────────────────────────────────────────|         
""")
    connection.commit()

def c_read():
    connection = connector()
    df = pd.read_sql("SELECT * FROM Customers", connection)
    print()
    print(df)
    print()
    connection.close()

def c_PhoneNo():
    connection = connector()
    Phone_No = input("Enter Updated phone no: ")
    C_ID = input("Enter Customer ID: ")

    cursor=connection.cursor()
    cursor.execute(f'UPDATE Customers SET Phone_No = {Phone_No} where C_ID = "{C_ID}"')
    connection.commit()
    print()
    print("Succesffuly Updated your Phone Number.")
    print()
    connection.close()


def c_update():
    c_PhoneNo()
    

def c_insert():
    connection = connector()
    C_ID = input("Enter your Customer ID: ")
    Cust_Name = input("Enter your name: ")
    Address = input("Enter your address: ")
    Phone_no = input("Enter your phone no: ")
    Adhar_no = input("Enter your adhar no: ")
    Arrival = input("Enter arrival date: ")
    Arrival_Date = int(Arrival[8] + Arrival[9])
    Arrival_Mnth = int(Arrival[5] + Arrival[6])
    Arrival_Year = int(Arrival[0] + Arrival[1] + Arrival[2] + Arrival[3])
    Departure = input("Enter departure date: ")
    Departure_Date = int(Departure[8] + Departure[9])
    Departure_Mnth = int(Departure[5] + Departure[6])
    Departure_Year = int(Departure[0] + Departure[1] + Departure[2] + Departure[3])
    Total_Stay = abs(datetime.date(Departure_Year, Departure_Mnth, Departure_Date) - datetime.date(Arrival_Year, Arrival_Mnth, Arrival_Date))
    Total_Stay = Total_Stay.days
    Room_no = input("Enter your room_no: ")
     
    Room_charge = pd.read_sql(f"SELECT room_charges FROM rooms where room_no = {Room_no}", connection)
    Room_charge = Room_charge.iloc[0,0]
    Total_pay = int(Total_Stay) * Room_charge
          
    cursor=connection.cursor()
    cursor.execute("INSERT into Customers values('{}', '{}', '{}', {}, {}, '{}', {})"
                    .format(C_ID, Cust_Name, Address, Phone_no, Adhar_no, Arrival, Room_no))
    cursor.execute(f"UPDATE Rooms SET Room_Status = 'Booked' where Room_no = {Room_no}")
    cursor.execute("insert into Bookings values('{}', '{}', {}, {}, '{}', '{}', {}, {}, {}, 'IN')"
                    .format(C_ID, Cust_Name, Adhar_no, Room_no, Arrival, Departure, Room_charge, Total_Stay, Total_pay))
     
    print()
    print(f"Successfully entered {Cust_Name} in the system.")
    print()
              
    connection.commit()
    connection.close()


def customers():    
    print()
    print("What do you want to do now?")
    print()
    print("""
            1 -----> See the list of rooms
            2 -----> Book a room
            3 -----> View your Customer Profile
            4 -----> Update your Profile
            5 -----> Checkout
            0 -----> Exit
""")
    Operation = input("Enter your choice: ")
    if Operation == '1':
        r_read()
    elif Operation == '2':
        c_insert()
    elif Operation == '3':
        cust_read()
    elif Operation == '4':
        c_update()
    elif Operation == '5':
        c_del()
    elif Operation == '0':
        quit()
    else:
        print()
        print('Enter a Valid option')

    redo = input("Do you wish to perform another task (y/n)? ")
    if redo == 'y':
        customers()
    else:
        quit()
