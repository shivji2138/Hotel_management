import tkinter as tk
import subprocess

def redirect(script_path):
    subprocess.run(['python', script_path])

#create mainwindow
app = tk.Tk()
app.title("Hotel Room Portal")
app.configure(bg="skyblue")
app.geometry("400x400")

#gui components
msg = tk.Label(app, text=''' Welcome to
Hotel Room Management
Portal''',bg='skyblue',font=('Helvetica',20))
msg.pack(pady=10)

button1 = tk.Button(app,bg="purple",fg="white",text ="ADD ROOM DETAILS",command=lambda: redirect('add_room_details.py'))
button1.pack(pady=10)

button2 = tk.Button(app,bg='purple',fg='white',text="RESERVE ROOM", command=lambda: redirect('reserve_room.py'))
button2.pack(pady=10)

#mainloop
app.mainloop()
