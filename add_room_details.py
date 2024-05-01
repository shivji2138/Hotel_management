import mysql.connector
import tkinter as tk
from tkinter import messagebox

# Connect to the database
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="shivusql",
    database="hotel_management"
)
cursor = mydb.cursor()

#Function to insert room details
def insert_details():
    try:
        room_num = int(roomnum_entry.get())
        capacity = int(capacity_entry.get())
        price = float(price_entry.get())
        availablity = bool(availablity_entry.get())
        cursor.execute("INSERT INTO rooms VALUES (%s,%s,%s,%s)",(room_num,capacity,price,availablity))
        mydb.commit()
        messagebox.showinfo("Success","Data Inserted Successfully")
    except mysql.connector.Error as err:
        messagebox.showerror("Failed",f"Error:{err}")

#tkinter window
app = tk.Tk()
app.title("Room Details")
app.configure(bg="skyblue")

#gui components

roomnum_label = tk.Label(app, bg="skyblue", text="Room Num:")
roomnum_label.grid(pady=10, padx=5, row=0,column=0)
roomnum_entry = tk.Entry(app)
roomnum_entry.grid(pady=10,padx=5,row=0,column=1)

capacity_label = tk.Label(app,bg="skyblue", text="Capacity:")
capacity_label.grid(pady=10, padx=5,row=1,column=0)
capacity_entry = tk.Entry(app)
capacity_entry.grid(pady=10,padx=5,row=1,column=1)

price_label = tk.Label(app, bg="skyblue", text="Price:")
price_label.grid(pady=10,padx=5,row=2,column=0)
price_entry = tk.Entry(app)
price_entry.grid(pady=10,padx=5,row=2,column=1)

availablity_label = tk.Label(app, bg="skyblue", text="Availablity:")
availablity_label.grid(pady=10,padx=5,row=3,column=0)
availablity_entry = tk.Entry(app)
availablity_entry.grid(pady=10,padx=5,row=3,column=1)

submit_button = tk.Button(app, bg="darkgreen",fg="white",text="SUBMIT",command=insert_details)
submit_button.grid(pady=10,padx=5,row=4,column=1,columnspan=2)



#mainloop
app.mainloop()
