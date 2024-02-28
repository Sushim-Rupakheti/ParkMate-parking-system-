from tkinter import *
from tkinter import messagebox
from tkinter import font

top = Tk()
top.geometry("1200x680")
top.title("Home Screen")
img=PhotoImage(file='photos/Unknown.png')
Label(top,image=img,border=0,bg='white').place(x=0,y=0)

def two_wheeler():
    messagebox.showinfo("Congratulations","Succesfully selected Two Wheeler")
    top.destroy()
    import Two_wheeler

def four_wheeler():
    messagebox.showinfo("Congratulations","Succesfully selected Four Wheeler")
    top.destroy()
    import Four_wheeler
    
label_font = font.Font(family='Helvetica', size=60, weight='bold')
label = Label(top, text="Select Vehicle Type:", font=label_font)
label.place(x=300, y=60)

button_font = font.Font(family='Arial', size=40)
two_wheeler_button = Button(top, text="Two Wheeler", font=button_font, width=15, command=two_wheeler)
two_wheeler_button.place(x=160, y=320)

four_wheeler_button = Button(top, text="Four Wheeler", font=button_font, width=15, command=four_wheeler)
four_wheeler_button.place(x=660, y=320)

def show_info(information):
    messagebox.showinfo("congratulations",f"A software program called a parking management system (PMS) app is made to simplify and enhance parking operations in a variety of settings,including garages,parkinng structures, and parking lots.With capabilities for effictive parking space distribution, payment processing,and real time monitoring,this kind of app benefits parking lot managers as well as car owner.")

button_font = font.Font(family='Arial', size=40)
show_info_button = Button(top, text="Info of Parkmate", font=button_font, width=15, command=lambda: show_info("information"))
show_info_button.place(x=430, y=500)

top.mainloop()