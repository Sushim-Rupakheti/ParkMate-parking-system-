from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from PIL import Image,ImageTk
import sqlite3
boot=Tk()
boot.configure(bg="grey")
boot.title("ParkMate")
icon_path = ("photos/bike.ico")
boot.iconbitmap(icon_path)

conn = sqlite3.connect("pk1.db")
cursor=conn.cursor()
cursor.execute("""CREATE TABLE IF NOT EXISTS parking(
          
          ID INTEGER PRIMARY KEY AUTOINCREMENT,
          
          VechileNo       TEXT,
          Type         TEXT,
          Time          INT,
          Cost          INT
          
          )""")
conn.commit()
conn.close()

bg = PhotoImage(file = "photos/color.png")  
labe001 = Label( boot, image = bg) 
labe001.place(x=500, y=70)
              
bg1 = PhotoImage(file = "photos/bike-2.png")  
labe001 = Label( boot, image = bg1) 
labe001.place(x= 0, y=70)


def add():
    vehicle_no=VechileNo.get()
    vehicle_type = Type.get()
    time = Time.get()
        
    if not vehicle_no or not vehicle_type or not time:
        messagebox.showerror("Error", "Please fill in all fields.")
        return
    try:
        time = int(time)
    except ValueError:
        messagebox.showerror("Error", "Time must be a valid integer.")
        return
    
    conn=sqlite3.connect('pk.db')
    c = conn.cursor()

    # Calculate cost based on vehicle type
    if vehicle_type == "Two Wheeler(Bicycle)":
        cost_per_hour = 25
    elif vehicle_type == "Two Wheeler(Bike)":
        cost_per_hour = 50
    elif vehicle_type == "Two Wheeler(Government)":
        cost_per_hour = 0
    else:
        cost_per_hour = 0

    cost = time * cost_per_hour

    c.execute("SELECT ID FROM parking ORDER BY ID ASC")
    records = c.fetchall()
    available_spaces = set(range(1, 21)) - set(record[0] for record in records)

    if available_spaces:
        space = min(available_spaces)
        c.execute("INSERT INTO parking (ID, VechileNo, Type, Time, Cost) VALUES (?, ?, ?, ?, ?)",
                  (space, VechileNo.get(), vehicle_type, time, cost))
    else:
        # If no available spaces, insert the new vehicle with ID incremented from the last ID
        c.execute("SELECT MAX(ID) FROM parking")
        last_id = c.fetchone()[0]
        new_id = last_id + 1 if last_id else 1
        c.execute("INSERT INTO parking (ID, VechileNo, Type, Time, Cost) VALUES (?, ?, ?, ?, ?)",
                  (new_id, VechileNo.get(), vehicle_type, time, cost))

    conn.commit()
    conn.close()
    messagebox.showinfo("Congratulations","Vehicle added successfully")
    VechileNo.delete(0, END)
    Type.set("") 
    Time.delete(0, END)






def Bill():
    import tkinter as Tk
    # Create a new window
    bill_window = Tk.Toplevel(boot)
    bill_window.title("Parking Bill")
    icon_path= ("C:/Users/mhnas/Desktop/LED/photos/bill.ico")
    bill_window.iconbitmap(icon_path)
    
    # Create Treeview widget
    tree = ttk.Treeview(bill_window, columns=("ID", "Column1", "Column2", "Column3", "Column4"), show="headings")
    tree.heading("ID", text="Parking Slot")
    tree.heading("Column1", text="Vehicle Number")
    tree.heading("Column2", text="Vechile Type")
    tree.heading("Column3", text="Time(In Hours)")
    tree.heading("Column4", text="Cost")
    tree.pack(fill="both", expand=True)
    
    # Connect to database and fetch data
    conn = sqlite3.connect("pk1.db")
    c = conn.cursor()
    c.execute("SELECT * FROM parking")
    records = c.fetchall()
    
    # Insert data into Treeview
    for record in records:
        tree.insert("", "end", values=record)
    
    conn.close()

def deleteRow():
    ID=delete.get()
    if not ID:
          messagebox.showerror("Error","Please enter the parking slot no of vehicle to be checked out")
          return
    
    conn = sqlite3.connect("pk1.db")
    c=conn.cursor()
    c.execute("DELETE FROM parking WHERE ID="+delete.get())
    conn.commit()
    conn.close
    delete.delete(0,END)
    Bill()
    



def edit(): 
          
          record_id =update_box.get()

          if not record_id:
                messagebox.showerror("Error","Please enter the parking slot of updating vehicle in entrybox below")
                return
           
          global editor
          editor = Tk()
          editor.iconbitmap(icon_path)
          editor.title('Update Vechile_Info')
          editor.geometry("300x300")
          editor.configure(bg="#FCE8E0")
          conn = sqlite3.connect("pk1.db")
          c=conn.cursor()

          c.execute("SELECT * FROM parking WHERE ID=?",(record_id,))
          
          # creating global variable
          global VechileNo_editor
          global Type_editor
          global Time_editor
          global Cost_editor
          
          records=c.fetchall()
          VechileNo_editor = Entry(editor,width=30)
          VechileNo_editor.grid(row=0,column=1,padx=20,pady=(10,0))
          Type_editor = Entry(editor,width=30)
          Type_editor.grid(row=1,column=1)
          Time_editor = Entry(editor,width=30)
          Time_editor.grid(row=2,column=1)
          Cost_editor = Entry(editor,width=30)
          Cost_editor.grid(row=3,column=1)
          
          VechileNo_label = Label(editor,text="VechileNo")
          VechileNo_label.grid(row=0,column=0,pady=(10,0))
          Type_label = Label(editor,text="Type")
          Type_label.grid(row=1,column=0)
          Time_label = Label(editor,text="Time")
          Time_label.grid(row=2,column=0)
          Cost_label = Label(editor,text="Cost")
          Cost_label.grid(row=3,column=0)
          for record in records:
                    VechileNo_editor.insert(0,record[1])
                    Type_editor.insert(0,record[2])
                    Time_editor.insert(0,record[3])
                    Cost_editor.insert(0,record[4])
          update_box.delete(0,END)
          save_btn = Button(editor,text="Save",command=lambda:update(record_id))
          save_btn.grid(column=0,row=6,columnspan=2,pady=10,padx=10,ipadx=125)
          

def update(record_id):
          conn = sqlite3.connect("pk1.db")
          c=conn.cursor()
          c.execute("""
                    UPDATE parking SET
                    VechileNo = :v,
                    Type  = :ty,
                    Time = :ti,
                    Cost = :c
                    WHERE ID = :id""",
                    {
                              "v":VechileNo_editor.get(),
                              'ty':Type_editor.get(),
                              'ti':Time_editor.get(),
                              'c':Cost_editor.get(),
                              "id":record_id  
                    }
                    )
          conn.commit()
          conn.close()
          messagebox.showinfo("congratulations","Vehicle_info successfully changed")
          
          
frame=LabelFrame(boot,padx=80,pady=80,bg="white")          
lbl = Label(text="ParkMate For 2-Wheelers",font=("Arial Bold",40),bg="grey").pack(pady=0)
boot.geometry("1200x680")
boot.resizable(0,0)

label_VechileNo = Label(text="Vechile no.",font=("Arial Bold",20),bg="#DCDFDE")
label_VechileNo.place(x=690,y=120)

label_Type = Label(text="Type",font=("Arial Bold",20),bg="#DCDFDE")
label_Type.place(x=690,y=190)

label_Time = Label(text="Time",font=("Arial Bold",20),bg="#DCDFDE")
label_Time.place(x=690,y=260)


label_delete = Label(text="Check out",font=("Arial Bold",20),bg="#DCDFDE")
label_delete.place(x=690,y=550)

label_update= Label(text="Update",font=("Arial Bold",20),bg="#DCDFDE")
label_update.place(x=690,y=500)

VechileNo = Entry(boot,width=30)
VechileNo.place(x=860,y=120,height=30)
VechileNo.configure(bg="#DCDFDE")

Type = ttk.Combobox(boot, width=27, values=["Two Wheeler(Bicycle)", "Two Wheeler(Bike)","Two Wheeler(Government)"])
Type.place(x=860, y=190, height=30)

Time = ttk.Combobox(boot, width=27, values=[1,2,3,4,5,6])
Time.place(x=860,y=260,height=30)


delete = ttk.Combobox(boot, width=27, values=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20])
delete.place(x=860,y=550,height=30)

update_box = Entry(boot, width=30)
update_box.place(x=860,y=500,height=30)
update_box.configure(bg="#DCDFDE")


add_btn= Button(boot,text="Add",font=("Arial Bold",20),command=add)
add_btn.place(x=660,y=350)


Bill_btn= Button(boot,text="Bill",font=("Arial Bold",20),command=Bill)
Bill_btn.place(x=750,y=350)

update_btn= Button(boot,text='Change Vechile \n Info',font =('Arial Bold',20),command=edit)
update_btn.place(x=850,y=350)

delete_btn= Button(boot,text="Check out",font=("Arial Bold",20),command=deleteRow)
delete_btn.place(x=950,y=600)

def open():
        global my_img
        top=Toplevel()
        my_img=ImageTk.PhotoImage(Image.open("photos/bike_slot.png"))
        top.iconbitmap(icon_path)
        my_label=Label(top,image=my_img)
        my_label.pack(pady=0)
        btn=Button(top,text="Close Window",bg="black",fg="white",command=top.destroy)
        btn.pack()
btnn=Button(boot,text="open Slot BluePrint",command=open,bg="black",fg="white")
btnn.place(x=30,y=77)

def back():
      boot.destroy()
      import Home_screen

btnn1=Button(boot,text="Back",command=back,bg="black",fg="white")
btnn1.place(x=560,y=590)


boot.mainloop()