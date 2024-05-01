import mysql.connector
import tkinter as tk
from tkinter import messagebox
from datetime import datetime

# Connect to the database
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="shivusql",
    database="hotel_management"
)
cursor = mydb.cursor()

# Function to add a new room
def add_room(room_number, capacity, price, available=True):
    sql = "INSERT INTO rooms (room_number, capacity, price, available) VALUES (%s, %s, %s, %s)"
    cursor.execute(sql, (room_number, capacity, price, available))
    db.commit()

# Function to check room availability
def check_room_availability(room_number):
    sql = "SELECT available FROM rooms WHERE room_number = %s"
    cursor.execute(sql, (room_number,))
    result = cursor.fetchone()
    if result:
        return result[0]
    else:
        return None

# Function to reserve a room
def reserve_room(room_number, guest_name, check_in_date, check_out_date):
    sql = "INSERT INTO reservations (room_number, guest_name, check_in_date, check_out_date) VALUES (%s, %s, %s, %s)"
    cursor.execute(sql, (room_number, guest_name, check_in_date, check_out_date))
    mydb.commit()
    sql = "UPDATE rooms SET available = FALSE WHERE room_number = %s"
    cursor.execute(sql, (room_number,))
    mydb.commit()

# Function to get all reservations
def get_reservations():
    sql = "SELECT * FROM reservations"
    cursor.execute(sql)
    return cursor.fetchall()

# Function to close database connection
def close_connection():
    cursor.close()
    mydb.close()


def reserve_room_gui():
    room_number = int(entry_room_number.get())
    guest_name = entry_guest_name.get()
    check_in_date = entry_check_in_date.get()
    check_out_date = entry_check_out_date.get()
    try:
        check_in_date = datetime.strptime(check_in_date, "%Y-%m-%d").date()
        check_out_date = datetime.strptime(check_out_date, "%Y-%m-%d").date()
        if check_in_date >= check_out_date:
            raise ValueError
    except ValueError:
        messagebox.showerror("Error", "Invalid date format or check-out date should be after check-in date.")
        return

    if check_room_availability(room_number):
        reserve_room(room_number, guest_name, check_in_date, check_out_date)
        messagebox.showinfo("Success", "Room reserved successfully.")
    else:
        messagebox.showerror("Error", "Room is not available.")

# Create GUI
app = tk.Tk()
app.title("Room Reservation")
app.configure(bg="skyblue")

label_room_number = tk.Label(app, bg="skyblue", text="Room Number:")
label_room_number.grid(pady=10,padx=5,row=0,column=0)
entry_room_number = tk.Entry(app)
entry_room_number.grid(pady=10,padx=5,row=0,column=1)

label_guest_name = tk.Label(app, bg="skyblue", text="Guest Name:")
label_guest_name.grid(pady=10,padx=5,row=1,column=0)
entry_guest_name = tk.Entry(app)
entry_guest_name.grid(pady=10,padx=5,row=1,column=1)

label_check_in_date = tk.Label(app, bg="skyblue", text="Check-in Date (YYYY-MM-DD):")
label_check_in_date.grid(pady=10,padx=5,row=2,column=0)
entry_check_in_date = tk.Entry(app)
entry_check_in_date.grid(pady=10,padx=5,row=2,column=1)

label_check_out_date = tk.Label(app, bg="skyblue", text="Check-out Date (YYYY-MM-DD):")
label_check_out_date.grid(pady=10,padx=5,row=3,column=0)
entry_check_out_date = tk.Entry(app)
entry_check_out_date.grid(pady=10,padx=5,row=3,column=1)

button_reserve = tk.Button(app, bg="darkgreen",fg="white", text="Reserve Room", command=reserve_room_gui)
button_reserve.grid(pady=10,padx=5,row=4,column=0,columnspan=2)

app.mainloop()
