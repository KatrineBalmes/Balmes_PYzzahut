from tkinter import *
from tkinter import messagebox
import subprocess
import sqlite3

def login_user():
    if username.get() == '' or password.get() == '':
        messagebox.showerror('Error', 'All Fields Are Required')
    else:
        try:
            # Connect to SQLite database (it will be created if it doesn't exist)
            con = sqlite3.connect('userdata.db')
            mycursor = con.cursor()
        except sqlite3.Error as e:
            messagebox.showerror('Error', f'Connection is not established: {e}')
            return

        # Query to check if username and password match
        query = 'SELECT * FROM data WHERE username=? AND password=?'
        mycursor.execute(query, (username.get(), password.get()))
        row = mycursor.fetchone()

        if row is None:
            messagebox.showerror('Error', 'Invalid username or password')
        else:
            messagebox.showinfo('Welcome', 'Login is Successful')
            subprocess.Popen(["python", "OrderingSystem.py"])
        con.close()

root = Tk()
root.geometry('1500x820')
root.resizable(0, 0)
root.overrideredirect(1)  # Remove the system's default title bar
root.configure(bg="#B9331C")

# Center the window on the screen
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x_coordinate = (screen_width // 2) - (1500 // 2)  # Center horizontally
y_coordinate = (screen_height // 2) - (820 // 2)  # Center vertically
root.geometry(f'1500x820+{x_coordinate}+{y_coordinate}')

# Create custom title bar
def close_app():
    root.destroy()

title_bar = Frame(root, bg="#B9331C", relief="raised", bd=0, height=30)
title_bar.pack(side=TOP, fill=X)

title_label = Label(title_bar, text="Customer Login", bg="#B9331C", fg="white", font=("Arial", 12, "bold"))
title_label.pack(side=LEFT, padx=10)

close_button = Button(title_bar, text="✖", bg="#B9331C", fg="white", font=("Arial", 12, "bold"), border=0,command=close_app, cursor="hand2")
close_button.pack(side=RIGHT, padx=5)

# Rest of your UI code
Image = PhotoImage(file='CustomerBackground.png')
Label(root, image=Image, bg='white', border=0).place(x=0, y=30)  # Adjusted to fit below title bar

frame = Frame(root, width=350, height=350, bg="#B9331C")
frame.place(x=900, y=250)

heading = Label(root, text='USER LOGIN', fg='#57a1f8', font=('Microsoft YaHei UI Light', 23, 'bold'),
                bg="#B9331C")
heading.place(x=980, y=240)

def hide():
    openeye.config(file="image-removebg-preview (1).png")
    password.config(show='')
    eyeButton.config(command=show)

def show():
    openeye.config(file="image-removebg-preview (2).png")
    password.config(show='*')
    eyeButton.config(command=hide)

def sign_up():
    subprocess.Popen(["python", "Sign-Up.py"])
    root.quit()

def on_enter(e):
    username.delete(0, 'end')

def on_leave(e):
    name = username.get()
    if name == '':
        username.insert(0, 'Username')

username = Entry(frame, width=25, fg='black', border=0, bg="#B9331C", font=('Microsoft YaHei UI Light', 11))
username.place(x=30, y=80)
username.insert(0, 'Username')
username.bind('<FocusIn>', on_enter)
username.bind('<FocusOut>', on_leave)

Frame(frame, width=295, height=2, bg='black').place(x=25, y=107)

def on_enter(e):
    password.delete(0, 'end')

def on_leave(e):
    name = password.get()
    if name == '':
        password.insert(0, 'Password')


password = Entry(frame, width=25, fg='black', border=0, bg="#B9331C", font=('Microsoft YaHei UI Light', 11), show='*')
password.place(x=30, y=150)
password.insert(0, 'Password')
password.bind('<FocusIn>', on_enter)
password.bind('<FocusOut>', on_leave)

Frame(frame, width=295, height=2, bg='black').place(x=25, y=177)

openeye = PhotoImage(file='image-removebg-preview (2).png')
eyeButton = Button(frame, image=openeye, border=0, bg="#B9331C", activebackground='#B9331C', cursor='hand2', command=hide)
eyeButton.place(x=285, y=145)

Button(frame, width=39, pady=7, text='Sign in', bg='#57a1f8', fg='white', border=0, command=login_user).place(x=35, y=204)
label = Label(frame, text="Don't have an account?", fg='black', bg="#B9331C", font=('Microsoft YaHei UI Light', 9))
label.place(x=75, y=270)
sign_up = Button(frame, width=6, text='Sign up', border=0, activebackground="#B9331C", bg="#B9331C", cursor='hand2', fg='#57a1f8', command=sign_up)
sign_up.place(x=215, y=270)

root.mainloop()