# from tkinter import *
# from tkinter import ttk
# from PIL import Image, ImageTk
# import sqlite3
# root=Tk()
# root.configure(bg="#FCE8E0")
# root.title("ParkMate")
# conn = sqlite3.connect("pk.db")
# cursor=conn.cursor()
# cursor.execute("""CREATE TABLE IF NOT EXISTS parking(
          
#           ID INTEGER PRIMARY KEY AUTOINCREMENT,
          
#           VechileNo       TEXT,
#           Type         TEXT,
#           Time          INT,
#           Cost          INT
          
#           )""")
# conn.commit()
# conn.close()

# bg1 = PhotoImage(file="C:/Users/mhnas/Desktop/LED/photos/color.png")
# labe001 = Label( root, image = bg1) 
# labe001.place(x = 0, y = 70)

# bg = PhotoImage(file = "C:/Users/mhnas/Desktop/LED/photos/simple-bg.png")  
# label1 = Label( root, image = bg) 
# label1.place(x = 500, y = 70)


# def add():
#     conn = sqlite3.connect("pk.db")
#     c = conn.cursor()

#     # Get the vehicle type and time from the input fields
#     vehicle_type = Type.get()
#     time = int(Time.get())

#     # Calculate cost based on vehicle type
#     if vehicle_type == "Four Wheeler(Heavy)":
#         cost_per_hour = 50
#     elif vehicle_type == "Four Wheeler(Personal)":
#         cost_per_hour = 25
#     elif vehicle_type == "Four Wheeler(Government)":
#         cost_per_hour = 0
#     else:
#         # Default cost if vehicle type is not recognized
#         cost_per_hour = 0

#     cost = time * cost_per_hour

#     # Check for available spaces
#     c.execute("SELECT ID FROM parking ORDER BY ID ASC")
#     records = c.fetchall()
#     available_spaces = set(range(1, 21)) - set(record[0] for record in records)

#     if available_spaces:
#         # If there are available spaces, insert the new vehicle at the lowest available ID
#         space = min(available_spaces)
#         c.execute("INSERT INTO parking (ID, VechileNo, Type, Time, Cost) VALUES (?, ?, ?, ?, ?)",
#                   (space, VechileNo.get(), vehicle_type, time, cost))
#     else:
#         # If no available spaces, insert the new vehicle with ID incremented from the last ID
#         c.execute("SELECT MAX(ID) FROM parking")
#         last_id = c.fetchone()[0]
#         new_id = last_id + 1 if last_id else 1
#         c.execute("INSERT INTO parking (ID, VechileNo, Type, Time, Cost) VALUES (?, ?, ?, ?, ?)",
#                   (new_id, VechileNo.get(), vehicle_type, time, cost))

#     conn.commit()
#     conn.close()

#     VechileNo.delete(0, END)
#     Type.set("")  # Reset the vehicle type selection
#     Time.delete(0, END)
#     Cost.delete(0, END)





# def Bill():
#     import tkinter as Tk
#     # Create a new window
#     bill_window = Tk.Toplevel(root)
#     bill_window.title("Parking Bill")
    
#     # Create Treeview widget
#     tree = ttk.Treeview(bill_window, columns=("ID", "Column1", "Column2", "Column3", "Column4"), show="headings")
#     tree.heading("ID", text="Parking Slot")
#     tree.heading("Column1", text="Vehicle Number")
#     tree.heading("Column2", text="Vechile Type")
#     tree.heading("Column3", text="Time(In Hours)")
#     tree.heading("Column4", text="Cost")
#     tree.pack(fill="both", expand=True)
    
#     # Connect to database and fetch data
#     conn = sqlite3.connect("pk.db")
#     c = conn.cursor()
#     c.execute("SELECT * FROM parking")
#     records = c.fetchall()
    
#     # Insert data into Treeview
#     for record in records:
#         tree.insert("", "end", values=record)
    
#     conn.close()

# def deleteRow():
#           conn = sqlite3.connect("pk.db")
#           ID=delete.get()
#           c=conn.cursor()
#           c.execute("DELETE FROM parking WHERE ID="+delete.get())
#           conn.commit()
#           conn.close
#           delete.delete(0,END)
#           Bill()
    



# def edit():  
#           global editor
#           editor = Tk()
#           editor.title('Update Vechile_Info')
#           editor.geometry("300x300")
#           editor.configure(bg="#FCE8E0")
#           conn = sqlite3.connect("pk.db")
#           c=conn.cursor()
#           record_id =update_box.get()
#           c.execute("SELECT * FROM parking WHERE ID=?",(record_id,))
          
#           # creating global variable
#           global VechileNo_editor
#           global Type_editor
#           global Time_editor
#           global Cost_editor
          
#           records=c.fetchall()
#           VechileNo_editor = Entry(editor,width=30)
#           VechileNo_editor.grid(row=0,column=1,padx=20,pady=(10,0))
#           Type_editor = Entry(editor,width=30)
#           Type_editor.grid(row=1,column=1)
#           Time_editor = Entry(editor,width=30)
#           Time_editor.grid(row=2,column=1)
#           Cost_editor = Entry(editor,width=30)
#           Cost_editor.grid(row=3,column=1)
          
#           VechileNo_label = Label(editor,text="VechileNo")
#           VechileNo_label.grid(row=0,column=0,pady=(10,0))
#           Type_label = Label(editor,text="Type")
#           Type_label.grid(row=1,column=0)
#           Time_label = Label(editor,text="Time")
#           Time_label.grid(row=2,column=0)
#           Cost_label = Label(editor,text="Cost")
#           Cost_label.grid(row=3,column=0)
#           for record in records:
#                     VechileNo_editor.insert(0,record[1])
#                     Type_editor.insert(0,record[2])
#                     Time_editor.insert(0,record[3])
#                     Cost_editor.insert(0,record[4])
#           update_box.delete(0,END)
#           save_btn = Button(editor,text="Save",command=lambda:update(record_id))
#           save_btn.grid(column=0,row=6,columnspan=2,pady=10,padx=10,ipadx=125)
          

# def update(record_id):
#           conn = sqlite3.connect("pk.db")
#           c=conn.cursor()
#           c.execute("""
#                     UPDATE parking SET
#                     VechileNo = :v,
#                     Type  = :ty,
#                     Time = :ti,
#                     Cost = :c
#                     WHERE ID = :id""",
#                     {
#                               "v":VechileNo_editor.get(),
#                               'ty':Type_editor.get(),
#                               'ti':Time_editor.get(),
#                               'c':Cost_editor.get(),
#                               "id":record_id  
#                     }
#                     )
#           conn.commit()
#           conn.close()
          
          
# frame=LabelFrame(root,padx=80,pady=80,bg="white")          
# lbl = Label(text="Parking management System",font=("Arial Bold",40),bg="#FCE8E0").pack(pady=0)
# root.geometry("1200x680")
# root.resizable(0,0)
# label_VechileNo = Label(text="Vechile no.",font=("Arial Bold",20),bg="#DCDFDE")
# label_VechileNo.place(x=40,y=120)

# label_address = Label(text="Type",font=("Arial Bold",20),bg="#DCDFDE")
# label_address.place(x=40,y=170)

# label_role = Label(text="Time",font=("Arial Bold",20),bg="#DCDFDE")
# label_role.place(x=40,y=210)

# label_salary = Label(text="Cost",font=("Arial Bold",20),bg="#DCDFDE")
# label_salary.place(x=40,y=260)

# label_delete = Label(text="Check out",font=("Arial Bold",20),bg="#DCDFDE")
# label_delete.place(x=40,y=550)

# label_update= Label(text="Update",font=("Arial Bold",20),bg="#DCDFDE")
# label_update.place(x=40,y=500)

# VechileNo = Entry(root,width=30)
# VechileNo.place(x=210,y=120,height=30)
# VechileNo.configure(bg="#DCDFDE")

# Type = ttk.Combobox(root, width=27, values=["Four Wheeler(Heavy)", "Four Wheeler(Personal)","Four Wheeler(Government)"])
# Type.place(x=210, y=170, height=30)

# Time = ttk.Combobox(root, width=27, values=[1,2,3,4,5,6])
# Time.place(x=210,y=210,height=30)


# Cost = Entry(root,width=30)
# Cost.place(x=210,y=260,height=30)
# Cost.configure(bg="#DCDFDE")

# delete = ttk.Combobox(root, width=27, values=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20])
# delete.place(x=210,y=550,height=30)


# update_box = Entry(root, width=30)
# update_box.place(x=210,y=500,height=30)
# update_box.configure(bg="#DCDFDE")


# add_btn= Button(root,text="Add",font=("Arial Bold",20),command=add)
# add_btn.place(x=10,y=350)


# Bill_btn= Button(root,text="Bill",font=("Arial Bold",20),command=Bill)
# Bill_btn.place(x=100,y=350)

# # Bill = Entry(root,width=30)
# # Bill.place(x=150,y=430,height=30)


# update_btn= Button(root,text="Change Vechile \n Info ",font=("Arial Bold",20),command=edit)
# update_btn.place(x=200,y=350)

# delete_btn= Button(root,text="Check out",font=("Arial Bold",20),command=deleteRow)
# delete_btn.place(x=300,y=600)

# def open():
#         global my_img
#         top=Toplevel()
#         my_img= ImageTk.PhotoImage(Image.open("C:/Users/mhnas/Desktop/LED/photos/map.png"))
#         my_label=Label(top,image=my_img)
#         my_label.pack(pady=0)
#         btn=Button(top,text="Close Window",bg="black",fg="white",command=top.destroy)
#         btn.pack()
# btnn=Button(root,text="open Slot BluePrint",command=open,bg="black",fg="white")
# btnn.place(x=1005,y=77)


# root.mainloop()



from tkinter import *
from tkinter import messagebox
from tkinter import font

# Create the main window
top = Tk()
top.geometry("1200x680")

# Load the background image
# img=PhotoImage(file='unknown.png')
# Label(top,image=img,border=0,bg='white').place(x=0,y=0)

def show_vehicle_type(vehicle_type):
    messagebox.showinfo("Congratulations",f"Succesfully selected  {vehicle_type}")

# Create a label widget
label_font = font.Font(family='Helvetica', size=60, weight='bold')
label = Label(top, text="Select Vehicle Type:", font=label_font)
label.place(x=240, y=60)

# Create button for two-wheelers
button_font = font.Font(family='Arial', size=40)
two_wheeler_button = Button(top, text="Two Wheeler", font=button_font, width=15, command=lambda: show_vehicle_type("Two Wheeler"))
two_wheeler_button.place(x=100, y=320)

# Create button for four-wheelers
four_wheeler_button = Button(top, text="Four Wheeler", font=button_font, width=15, command=lambda: show_vehicle_type("Four Wheeler"))
four_wheeler_button.place(x=600, y=320)

top.mainloop()