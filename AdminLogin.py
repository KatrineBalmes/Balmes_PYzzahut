from tkinter import *
from tkinter import messagebox
import subprocess

root = Tk()
root.geometry('1500x820')
root.resizable(0, 0)
root.configure(bg="#B9331C")
root.overrideredirect(1)  # Remove the system's default title bar
# Center the window on the screen
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x_coordinate = (screen_width // 2) - (1500 // 2)  # Center horizontally
y_coordinate = (screen_height // 2) - (820 // 2)  # Center vertically
root.geometry(f'1500x820+{x_coordinate}+{y_coordinate}')

# Title bar
def close_app():
    root.destroy()


title_bar = Frame(root, bg="#B9331C", relief="raised", height=30)
title_bar.pack(side=TOP, fill=X)
title_label = Label(title_bar, text="Admin Login", bg="#B9331C", fg="white", font=("Arial", 12, "bold"))
title_label.pack(side=LEFT, padx=10)

close_button = Button(title_bar, text="X", bg="red", fg="white", font=("Arial", 12, "bold"), border=0, cursor="hand2", command=close_app)
close_button.pack(side=RIGHT, padx=5, pady=2)

# Background image
img = PhotoImage(file='AdminBg(1).png')
Label(root, image=img, bg='white',border=0).place(x=0, y=30)

# Frame for login
frame = Frame(root, width=500, height=350, bg="#B9331C")
frame.place(x=900, y=180)

# Heading
heading = Label(frame, text='Sign in', fg='#57a1f8', bg="#B9331C", font=('Microsoft YaHei UI Light', 23, 'bold'))
heading.place(x=150, y=75)
# Username entry field with focus in/out handlers
def on_enter_username(e):
    user.delete(0, 'end')

def on_leave_username(e):
    name = user.get()
    if name == '':
        user.insert(0, 'Username')

user = Entry(frame, width=25, fg='black', border=0, bg="#B9331C", font=('Microsoft YaHei UI Light', 11))
user.place(x=60, y=150)
user.insert(0, 'Username')
user.bind('<FocusIn>', on_enter_username)
user.bind('<FocusOut>', on_leave_username)

# Border for username entry
Frame(frame, width=295, height=2, bg='black').place(x=60, y=170)

# Password entry field with focus in/out handlers
def on_enter_password(e):
    key.delete(0, 'end')

def on_leave_password(e):
    name = key.get()
    if name == '':
        key.insert(0, 'Password')

key = Entry(frame, width=25, fg='black', border=0, bg="#B9331C", font=('Microsoft YaHei UI Light', 11), show="*")
key.place(x=60, y=200)
key.insert(0, 'Password')
key.bind('<FocusIn>', on_enter_password)
key.bind('<FocusOut>', on_leave_password)

# Border for password entry
Frame(frame, width=295, height=2, bg='black').place(x=60, y=220)

# Sign-in button
def signin():
    username = user.get()
    password = key.get()

    if username == 'admin' and password == 'Pyzzword':
        messagebox.showinfo("Login", "Login Successful")
        subprocess.Popen(["python", "Dashboard_1.py"])
        root.quit()
    elif username != 'admin' and password != 'Pyzzword':
        messagebox.showerror("Invalid", "Invalid username and password")
    elif password != "Pyzzword":
        messagebox.showerror("Invalid", "Invalid password")
    elif username != 'admin':
        messagebox.showerror("Invalid", "Invalid username")

Button(frame, width=39, pady=7, text='Sign in', bg='#57a1f8', fg='white', border=0, command=signin).place(x=70, y=260)

root.mainloop()