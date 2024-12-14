from tkinter import *
from tkinter import messagebox
from PIL import Image
import time
import subprocess


class AdminDashboard:
    def __init__(self, root):
        self.root = root
        self.root.geometry('1500x820')
        self.root.title('Admin Dashboard')
        self.root.resizable(0, 0)
        self.root.configure(bg="white")
        self.root.overrideredirect(1)  # Removes window border

        # Center the window
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        x_coordinate = (screen_width // 2) - (1500 // 2)
        y_coordinate = (screen_height // 2) - (820 // 2)
        self.root.geometry(f'1500x820+{x_coordinate}+{y_coordinate}')

        # Track the selected button
        self.selected_button = None
        self.current_subprocess = None  # Track the current subprocess

        # Title (Center)
        title = Label(self.root, text="PYzzahut", fg='white', width=100, font=('Verdana', 40, "bold"), bg="#B9331C")
        title.place(relx=0.5, y=0, anchor="n", height=70)

        self.display_frame = Frame(self.root, bg="peru", border=3, relief=RIDGE)
        self.display_frame.place(x=200, y=200, height=300, width=300)

        # Logout Button
        self.btn_logout = PhotoImage(file='logout.png')
        btn_logout = Button(self.root, image=self.btn_logout, border=0, bg="#B9331C",
                            activebackground="#B9331C", cursor="hand2", command=self.logout)
        btn_logout.place(x=1370, y=20, width=180, height=40)

        # Background Left Image
        self.left_pic = self.load_image("dboardbg.png")
        if self.left_pic:
            picture = Label(self.root, image=self.left_pic, bg="black")
            picture.place(x=0, y=80, height=1000)

        # Category Buttons
        btn_Overall = Button(self.root, text="Overall Category", font=('Verdana', 15, 'bold'), bg="brown",cursor="hand2", command=lambda: [self.select_button(btn_Overall), self.Overall()])
        btn_Overall.place(x=190, y=100, width=282, height=60)

        btn_Employee = Button(self.root, text="Employee", font=('Verdana', 15, 'bold'), bg="brown", cursor="hand2", command=lambda: [self.select_button(btn_Employee), self.Employee()])
        btn_Employee.place(x=450, y=100, width=350, height=60)

        btn_Product = Button(self.root, text="Product/Stocks", font=('Verdana', 15, 'bold'), bg="brown", cursor="hand2", command=lambda: [self.select_button(btn_Product), self.Products()])
        btn_Product.place(x=800, y=100, width=350, height=60)

        btn_Sales = Button(self.root, text="Sales", font=('Verdana', 15, 'bold'), bg="brown", cursor="hand2",command=lambda: [self.select_button(btn_Sales), self.Sales()])
        btn_Sales.place(x=1150, y=100, width=400, height=60)

        # Create frames (initialized but not displayed initially)
        self.overall_frame = Frame(self.root, bg="peru", border=3, relief=RIDGE)
        self.emp_frame = Frame(self.root, bg="peru", border=3, relief=RIDGE)
        self.product_frame = Frame(self.root, bg="peru", border=3, relief=RIDGE)
        self.sales_frame = Frame(self.root, bg="peru", border=3, relief=RIDGE)

        # Clock showing Date and Time
        self.clock = Label(self.root, text="Welcome to Pyzzahut! Date: DD-MM-YYYY Time: HH:MM:SS", font=("Verdana", 15), bg="black", fg="white")
        self.clock.place(x=0, y=70, relwidth=1, height=30)
        self.update_clock()

    def load_image(self, filepath):
        """ Attempt to load an image and handle exceptions. """
        try:
            return PhotoImage(file=filepath)
        
        except Exception as e:
            print(f"Error loading image '{filepath}': {e}")
            return None  # Use a default or placeholder image if needed
        
        

    def update_clock(self):
        """ Update the clock every second. """
        current_time = time.strftime('%H:%M:%S')
        current_date = time.strftime('%d-%m-%Y')
        self.clock.config(text=f"Welcome to Pyzzahut!  Date: {current_date}  Time: {current_time}")
        self.clock.after(1000, self.update_clock)

    def logout(self):
        """ Logout functionality (close the dashboard). """
        result = messagebox.askyesno("Logout", "Are you sure you want to log out?")
        if result:
            subprocess.Popen(["python", "WelcomePage.py"])
            self.root.quit()

    def select_button(self, button):
        """ Highlight the selected button and reset others. """
        if self.selected_button:
            self.selected_button.config(bg="brown")
        button.config(bg="Peru")
        self.selected_button = button

    def close_current_subprocess(self):
        """Terminate the current subprocess if it exists."""
        if hasattr(self, 'current_subprocess') and self.current_subprocess:
            try:
                self.current_subprocess.terminate()  # Terminate the process
                self.current_subprocess.wait()      # Wait for the process to finish
                self.current_subprocess = None      # Reset the variable
            except Exception as e:
                print(f"Error closing subprocess: {e}")

    def Overall(self):
        """ Open the Overall Category window. """
        self.close_current_subprocess()  # Close any existing subprocess
        self.current_subprocess = subprocess.Popen(["python", "OverallCategory.py"])

    def Employee(self):
        """ Open the Employee window. """
        self.close_current_subprocess()  # Close any existing subprocess
        self.current_subprocess = subprocess.Popen(["python", "Employee.py"])

    def Products(self):
        """ Open the Product/Stocks window. """
        self.close_current_subprocess()  # Close any existing subprocess
        self.current_subprocess = subprocess.Popen(["python", "Products.py"])

    def Sales(self):
        """ Open the Sales window. """
        self.close_current_subprocess()  # Close any existing subprocess
        self.current_subprocess = subprocess.Popen(["python", "Sales.py"])


if __name__ == "__main__":
    root = Tk()
    admin_dashboard = AdminDashboard(root)
    root.mainloop()
