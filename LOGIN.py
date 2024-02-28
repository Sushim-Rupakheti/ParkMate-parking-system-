from tkinter import *
from tkinter import messagebox
import sqlite3

conn = sqlite3.connect('user_data.db')
cursor = conn.cursor()


cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        username TEXT PRIMARY KEY,
        password TEXT
    )
''')
conn.commit()

root = Tk()
root.title('Login')
icon_path = "photos/car.ico"
root.iconbitmap(icon_path)
root.geometry('1200x680')
root.configure(bg="#fff")
root.resizable(False, False)


def signin():
    username = user.get()
    password = code.get()

    cursor.execute("SELECT * FROM users WHERE username=? AND password=?", (username, password))
    result = cursor.fetchone()

    if result:
        root.destroy()
        import Home_screen
    else:
        messagebox.showerror('Invalid', 'Invalid username or password')

def signup_command():
    window = Toplevel(root)
    window.title("SignUp")
    window.iconbitmap(icon_path)
    window.geometry('1200x680')
    window.configure(bg='#fff')
    window.resizable(False, False)

    def signup():
        username = user.get()
        password = code.get()
        confirm_password = confirm_code.get()

        if password == confirm_password:
            try:
                cursor.execute("INSERT INTO users VALUES (?, ?)", (username, password))
                conn.commit()

                messagebox.showinfo('SignUp', 'Successfully signed up')
                window.destroy()

            except sqlite3.IntegrityError:
                messagebox.showerror('Invalid', 'Username already exists')

        else:
            messagebox.showerror('Invalid', "Both passwords should match")

    def sign():
        window.destroy()

    img = PhotoImage(file="photos/parkmate.png")
    Label(window, image=img, border=0, bg='white').place(x=2, y=10)

    heading = Label(window, text='Sign Up', fg='black', bg='white', font=('Microsoft YaHei UI Light', 23, 'bold'))
    heading.place(x=545, y=150)

    def on_enter(e):
        user.delete(0, 'end')

    def on_leave(e):
        if user.get() == '':
            user.insert(0, 'Username')

    user = Entry(window, width=35, fg='black', border=0, bg="white", font=('Microsoft YaHei UI Light', 11))
    user.place(x=460, y=250)
    user.insert(0, 'Username')
    user.bind('<FocusIn>', on_enter)
    user.bind('<FocusOut>', on_leave)

    Frame(window, width=295, height=2, bg='black').place(x=455, y=277)

    def on_enter(e):
        code.delete(0, 'end')

    def on_leave(e):
        if code.get() == '':
            code.insert(0, 'Password')

    code = Entry(window, width=35, fg='black', border=0, bg="white", font=('Microsoft YaHei UI Light', 11))
    code.place(x=460, y=320)
    code.insert(0, 'Password')
    code.bind('<FocusIn>', on_enter)
    code.bind('<FocusOut>', on_leave)

    Frame(window, width=295, height=2, bg='black').place(x=455, y=347)

    def on_enter(e):
        confirm_code.delete(0, 'end')

    def on_leave(e):
        if confirm_code.get() == '':
            confirm_code.insert(0, 'Confirm Password')

    confirm_code = Entry(window, width=35, fg='black', border=0, bg="white", font=('Microsoft YaHei UI Light', 11))
    confirm_code.place(x=460, y=390)
    confirm_code.insert(0, 'Confirm Password')
    confirm_code.bind('<FocusIn>', on_enter)
    confirm_code.bind('<FocusOut>', on_leave)

    Frame(window, width=295, height=2, bg='black').place(x=455, y=417)

    Button(window, width=39, pady=7, text='Sign Up', bg='black', fg='white', border=0, command=signup).place(x=465, y=450)
    label = Label(window, text='I have an account!', fg='black', bg='white', font=('Microsoft YaHei UI Light', 9))
    label.place(x=510, y=510)

    signin_btn = Button(window, width=6, text='Sign In', border=0, bg='white', cursor='hand2', fg='black', command=sign)
    signin_btn.place(x=615, y=511)

    window.mainloop()

img = PhotoImage(file="photos/parkmate.png")
Label(root, image=img, bg='white').place(x=2, y=10)

heading = Label(text='Sign In', fg='black', bg='white', font=('Microsoft YaHei UI Light', 23, 'bold'))
heading.place(x=545, y=150)

def on_enter(e):
    user.delete(0, 'end')

def on_leave(e):
    name = user.get()
    if name == '':
        user.insert(0, 'Username')

user = Entry(width=25, fg='black', border=0, bg="white", font=('Microsoft YaHei UI Light', 11))
user.place(x=460, y=250)
user.insert(0, 'Username')
user.bind('<FocusIn>', on_enter)
user.bind('<FocusOut>', on_leave)

Frame(width=295, height=2, bg='black').place(x=455, y=277)

def on_enter(e):
    code.delete(0, 'end')

def on_leave(e):
    name = code.get()
    if name == '':
        code.insert(0, 'Password')

code = Entry(width=25, fg='black', border=0, bg="white", font=('Microsoft YaHei UI Light', 11))
code.place(x=460, y=320)
code.insert(0, 'Password')
code.bind('<FocusIn>', on_enter)
code.bind('<FocusOut>', on_leave)

Frame(width=295, height=2, bg='black').place(x=455, y=347)

Button(width=39, pady=7, text='Sign In', bg='black', fg='white', border=0, command=signin).place(x=465, y=380)
label = Label(text="Don't have an account?", border=0, bg='white', font=('Microsoft YaHei UI Light', 9))
label.place(x=510, y=440)

sign_up = Button(width=6, text='Sign Up', border=0, bg='white', cursor='hand2', fg='black', command=signup_command)
sign_up.place(x=645, y=440)

root.mainloop()