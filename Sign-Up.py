from tkinter import *
from tkinter import messagebox
import sqlite3
import subprocess

def clear():
    emailEntry.delete(0, END)
    userEntry.delete(0, END)
    passwordEntry.delete(0, END)
    confirmEntry.delete(0, END)
    check.set(0)

def connect_database():
    if emailEntry.get() == '' or userEntry.get() == '' or passwordEntry.get() == '' or confirmEntry.get() == '':
        messagebox.showerror('Error', 'All Fields are Required')
    elif passwordEntry.get() != confirmEntry.get():
        messagebox.showerror('Error', 'Password Mismatch')
    elif check.get() == 0:
        messagebox.showerror('Error', 'Please Accept Terms & Conditions')
    else:
        try:
            # Connect to SQLite database (creates file if it doesn't exist)
            con = sqlite3.connect('userdata.db')
            cursor = con.cursor()

            # Create the table if it doesn't already exist
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS data (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    email TEXT NOT NULL,
                    username TEXT UNIQUE NOT NULL,
                    password TEXT NOT NULL
                )
            ''')

            # Check if username already exists
            cursor.execute('SELECT * FROM data WHERE username = ?', (userEntry.get(),))
            row = cursor.fetchone()
            if row is not None:
                messagebox.showerror('Error', 'Username Already Exists')
            else:
                # Insert new user into the database
                cursor.execute('INSERT INTO data (email, username, password) VALUES (?, ?, ?)',(emailEntry.get(), userEntry.get(), passwordEntry.get()))
                con.commit()
                con.close()
                messagebox.showinfo('Success', 'Registration is Successful')
                clear()
                root.destroy()
                subprocess.Popen(["python", "CustomerLogin.py"])
        except sqlite3.Error as e:
            messagebox.showerror('Error', f'Database Error: {e}')

def signup_page():
    subprocess.Popen(["python", "CustomerLogin.py"])
    root.quit()

root = Tk()
root.geometry('1500x820')
root.resizable(0, 0)
root.configure(bg="#B9331C")
root.overrideredirect(1)

# Center the window on the screen
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x_coordinate = (screen_width // 2) - (1500 // 2)
y_coordinate = (screen_height // 2) - (820 // 2)
root.geometry(f'1500x820+{x_coordinate}+{y_coordinate}')

# Title bar
title_bar = Frame(root, bg="#B9331C", relief="raised", height=30)
title_bar.pack(side=TOP, fill=X)
title_label = Label(title_bar, text="Sign-Up", bg="#B9331C", fg="white", font=("Arial", 12, "bold"))
title_label.pack(side=LEFT, padx=10)

close_btn = Button(title_bar, text="X", font=("Verdana", 10, "bold"), bg="red", fg="white", border=0, cursor="hand2", command=root.destroy)
close_btn.pack(side=RIGHT, padx=5, pady=2)

# Background image
root.background_image = PhotoImage(file='AdminCustomerBg.png')
background_label = Label(root, image=root.background_image, bg='brown')
background_label.place(x=0, y=30)

# Frame for login
frame = Frame(root, width=500, height=350, bg="#B9331C")
frame.place(x=900, y=180)

# Heading
heading = Label(frame, text='CREATE AN ACCOUNT', fg='#57a1f8', bg="#B9331C", font=('Microsoft YaHei UI Light', 23, 'bold'))
heading.grid(row=0, column=0)

# Form fields
emailLabel = Label(frame, text="Email", fg='black', bg="#B9331C", font=('Verdana', 11))
emailLabel.grid(row=1, column=0, sticky='w', padx=25, pady=(10, 0))
emailEntry = Entry(frame, width=25, font=('Verdana', 11))
emailEntry.grid(row=2, column=0, sticky='w', padx=25)

userLabel = Label(frame, text="Username", fg='black', bg="#B9331C", font=('Verdana', 11))
userLabel.grid(row=3, column=0, sticky='w', padx=25, pady=(10, 0))
userEntry = Entry(frame, width=25, font=('Verdana', 11))
userEntry.grid(row=4, column=0, sticky='w', padx=25)

passwordLabel = Label(frame, text="Password", fg='black', bg="#B9331C", font=('Verdana', 11))
passwordLabel.grid(row=5, column=0, sticky='w', padx=25, pady=(10, 0))
passwordEntry = Entry(frame, width=25, font=('Verdana', 11), show='*')
passwordEntry.grid(row=6, column=0, sticky='w', padx=25)

confirmLabel = Label(frame, text="Confirm Password", fg='black', bg="#B9331C", font=('Verdana', 11))
confirmLabel.grid(row=7, column=0, sticky='w', padx=25, pady=(10, 0))
confirmEntry = Entry(frame, width=25, font=('Verdana', 11), show='*')
confirmEntry.grid(row=8, column=0, sticky='w', padx=25)

# Terms & Conditions
check = IntVar()
termsandconditions = Checkbutton(frame, text='I agree to the Terms & Conditions',font=('Verdana', 9, 'bold'), bg="#B9331C",variable=check)
termsandconditions.grid(row=9, sticky='w', column=0, pady=10, padx=15)

# Buttons
signupButton = Button(frame, text='Sign-up', font=('Verdana', 11, 'bold'), border=0, activebackground='#57a1f8', bg='#57a1f8', cursor='hand2', width=25, command=connect_database)
signupButton.grid(row=10, column=0, sticky='w', padx=25, pady=(10, 0))

haveaccount = Label(frame, text='Already have an account?', font=('Verdana', 8), border=0,
                    activebackground="#B9331C", bg="#B9331C", width=25, height=3)
haveaccount.grid(row=11, column=0, sticky='w', padx=30)

loginBlue = Button(frame, text='Log In', font=('Verdana', 8), border=0,activebackground="#B9331C", bg="#B9331C", fg='#57a1f8',cursor='hand2', width=5, height=1, command=signup_page)
loginBlue.place(x=195, y=364)

root.mainloop()