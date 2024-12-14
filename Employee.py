from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import sqlite3
import re

class employeeClass:
    def __init__(self, root):
        self.root = root
        self.root.geometry('1310x650+208+182')
        self.root.title('Employee')
        self.root.configure(bg="#B9331C")
        self.root.focus_force()
        self.root.overrideredirect(1)

        # Database connection
        self.connect_database()

        # All Variables
        self.var_searchby = StringVar()
        self.var_searchtxt = StringVar()

        self.var_emp_id = StringVar()
        self.var_gender = StringVar()
        self.var_contact = StringVar()
        self.var_name = StringVar()
        self.var_dob = StringVar()
        self.var_de = StringVar()
        self.var_email = StringVar()
        self.var_role = StringVar()
        self.var_salary = StringVar()

        # Text Address Widget (not a StringVar)
        self.txt_address = None

        # Custom title bar
        title_bar = Frame(self.root, bg="brown", relief=RAISED, height=30)
        title_bar.pack(side=TOP, fill=X)
        title_label = Label(title_bar, text="Employee Details", font=("Verdana", 18, "bold"), bg="brown", fg="white")
        title_label.pack(side=LEFT, padx=10)

        # Search frame
        SearchFrame = LabelFrame(self.root, text="Search Employee", font=("Verdana", 13, "bold"), relief=RIDGE,bg="#B9331C", fg="white")
        SearchFrame.place(x=10, y=40, width=600, height=60)

        combo_search = ttk.Combobox(SearchFrame, textvariable=self.var_searchby,
                                    values=("Select", "Email", "Name", "Contact"), state='readonly', justify=CENTER,
                                    font=("Verdana", 12))
        combo_search.place(x=10, y=3, width=150)
        combo_search.current(0)

        Entry(SearchFrame, textvariable=self.var_searchtxt, font=("Verdana", 12), bg="light yellow").place(x=180, y=3,width=220,height=25)
        Button(SearchFrame, text="Search", font=("Verdana", 12), bg="brown", fg="white", cursor="hand2",command=self.search).place(x=430, y=3, width=150, height=25)

        # Design separator
        Label(self.root, bg="brown").place(x=0, y=110, width=1400, height=20)

        # Content
        # Row 1
        Label(self.root, text="Employee ID", font=("Verdana", 15), bg="#B9331C").place(x=85, y=150)
        Label(self.root, text="Gender", font=("Verdana", 15), bg="#B9331C").place(x=530, y=150)
        Label(self.root, text="Contact", font=("Verdana", 15), bg="#B9331C").place(x=885, y=150)

        Entry(self.root, textvariable=self.var_emp_id, font=("Verdana", 10), bg="light yellow").place(x=230, y=150,width=250,height=30)
        combo_gender = ttk.Combobox(self.root, textvariable=self.var_gender, values=("Select", "Male", "Female", "Other"),
                                    state='readonly', justify=CENTER, font=("Verdana", 10))
        combo_gender.place(x=650, y=150, width=180, height=30)
        combo_gender.current(0)
        Entry(self.root, textvariable=self.var_contact, font=("Verdana", 10), bg="light yellow").place(x=1050, y=150,width=220,height=30)

        # Row 2
        Label(self.root, text="Name", font=("Verdana", 15), bg="#B9331C").place(x=85, y=200)
        Label(self.root, text="Birthdate", font=("Verdana", 15), bg="#B9331C").place(x=530, y=200)
        Label(self.root, text="Date Employed", font=("Verdana", 15), bg="#B9331C").place(x=885, y=200)

        Entry(self.root, textvariable=self.var_name, font=("Verdana", 10), bg="light yellow").place(x=230, y=200,width=250, height=30)
        Entry(self.root, textvariable=self.var_dob, font=("Verdana", 10), bg="light yellow").place(x=650, y=200,width=180,height=30)
        Entry(self.root, textvariable=self.var_de, font=("Verdana", 10), bg="light yellow").place(x=1050, y=200, width=220,height=30)

        # Row 3
        Label(self.root, text="Email", font=("Verdana", 15), bg="#B9331C").place(x=85, y=250)
        Label(self.root, text="Role", font=("Verdana", 15), bg="#B9331C").place(x=530, y=250)
        Label(self.root, text="Salary", font=("Verdana", 15), bg="#B9331C").place(x=885, y=250)

        Entry(self.root, textvariable=self.var_email, font=("Verdana", 10), bg="light yellow").place(x=230, y=250, width=250,height=30)
        combo_role = ttk.Combobox(self.root, textvariable=self.var_role, values=("Select", "Delivery Driver","Pizza Maker", "Manager"),
                                                    state='readonly', justify=CENTER, font=("Verdana", 10))
        combo_role.place(x=650, y=250, width=180, height=30)
        combo_role.current(0)
        Entry(self.root, textvariable=self.var_salary, font=("Verdana", 10), bg="light yellow").place(x=1050, y=250,width=220,height=30)

        # Row 4
        Label(self.root, text="Address", font=("Verdana", 15), bg="#B9331C").place(x=85, y=300)
        self.txt_address = Text(self.root, font=("Verdana", 10), bg="light yellow")
        self.txt_address.place(x=230, y=300, width=250, height=90)

        # Buttons
        Button(self.root, text="Save", font=("Verdana", 15), bg="brown", fg="white", cursor="hand2",command=self.add_employee).place(x=520, y=320, width=150, height=35)
        Button(self.root, text="Update", font=("Verdana", 15), bg="brown", fg="white", cursor="hand2",command=self.update_employee).place(x=720, y=320, width=150, height=35)
        Button(self.root, text="Delete", font=("Verdana", 15), bg="brown", fg="white", cursor="hand2",command=self.delete_employee).place(x=920, y=320, width=150, height=35)
        Button(self.root, text="Clear", font=("Verdana", 15), bg="brown", fg="white", cursor="hand2",command=self.clear_fields).place(x=1120, y=320, width=150, height=35)

        # Employee Details
        emp_frame = Frame(self.root, border=3, relief=RIDGE)
        emp_frame.place(x=0, y=395, relwidth=1, height=235)

        # Scrollbars
        scrolly = Scrollbar(emp_frame, orient=VERTICAL)
        scrollx = Scrollbar(emp_frame, orient=HORIZONTAL)

        # Treeview (Employee Table)
        self.EmployeeTable = ttk.Treeview(emp_frame, columns=("Eid", "name", "email", "gender", "Cont", "DOB", "DE", "role", "address", "salary"),yscrollcommand=scrolly.set, xscrollcommand=scrollx.set)

        # Packing Scrollbars
        scrolly.pack(side=RIGHT, fill=Y)
        scrollx.pack(side=BOTTOM, fill=X)

        # Configuring Scrollbars to Control Treeview
        scrolly.config(command=self.EmployeeTable.yview)
        scrollx.config(command=self.EmployeeTable.xview)

        # Treeview Configuration
        self.EmployeeTable.heading("Eid", text="Employee ID")
        self.EmployeeTable.heading("name", text="Name")
        self.EmployeeTable.heading("email", text="Email")
        self.EmployeeTable.heading("gender", text="Gender")
        self.EmployeeTable.heading("Cont", text="Contact No.")
        self.EmployeeTable.heading("DOB", text="Date of Birth")
        self.EmployeeTable.heading("DE", text="Date Employed")
        self.EmployeeTable.heading("role", text="Role")
        self.EmployeeTable.heading("address", text="Address")
        self.EmployeeTable.heading("salary", text="Salary")

        self.EmployeeTable['show'] = 'headings'

        self.EmployeeTable.column("Eid", width=100)
        self.EmployeeTable.column("name", width=200)
        self.EmployeeTable.column("email", width=250)
        self.EmployeeTable.column("gender", width=150)
        self.EmployeeTable.column("Cont", width=150)
        self.EmployeeTable.column("DOB", width=150)
        self.EmployeeTable.column("DE", width=150)
        self.EmployeeTable.column("role", width=150)
        self.EmployeeTable.column("address", width=250)
        self.EmployeeTable.column("salary", width=150)

        self.EmployeeTable.pack(fill=BOTH, expand=1)

        self.fetch_data()

    def connect_database(self):
        self.conn = sqlite3.connect("employee.db")
        self.cursor = self.conn.cursor()
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS employees (
                emp_id INTEGER PRIMARY KEY,
                name TEXT,
                email TEXT,
                gender TEXT,
                contact TEXT,
                dob TEXT,
                date_employed TEXT,
                role TEXT,
                address TEXT,
                salary REAL
            )
        """)
        self.conn.commit()

    def validate_employee_data(self, name, email, gender, contact, dob, de, role, address, salary):

        if not name or not email or not gender or not contact or not dob or not de or not role or not address or not salary:
                return "All fields are required!"
        if len(contact) != 10 or not contact.isdigit():
                return "Contact number must be 11 digits!"
        if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
                return "Invalid email format!"
        try:
                month, day, year = map(int, dob.split("/"))
                if not (1 <= month <= 12) or not (1 <= day <= 31) or not (1900 <= year <= 2100):
                        return "Invalid date of birth format. Use MM/DD/YYYY."
        except ValueError:
                return "Invalid date of birth format. Use MM/DD/YYYY."

        try:
                month, day, year = map(int, de.split("/"))
                if not (1 <= month <= 12) or not (1 <= day <= 31) or not (1900 <= year <= 2100):
                        return "Invalid Date Employed format. Use MM/DD/YYYY."
        except ValueError:
                return "Invalid Date Employed format. Use MM/DD/YYYY."

        try:
                salary = float(salary)
                if salary <= 0:
                        return "Salary must be a positive number!"
        except ValueError:
                return "Salary must be a number!"

        return None  # No validation error

    def add_employee(self):
        name = self.var_name.get()
        email = self.var_email.get()
        gender = self.var_gender.get()
        contact = self.var_contact.get()
        dob = self.var_dob.get()
        de = self.var_de.get()
        role = self.var_role.get()
        salary = self.var_salary.get()
        address = self.txt_address.get("1.0", "end-1c")

        error_message = self.validate_employee_data(name, email, gender, contact, dob, de, role, address, salary)
        if error_message:
            messagebox.showerror("Error", error_message)
            return
        
        # Insert data into the database
        self.cursor.execute("""
            INSERT INTO employees (name, email, gender, contact, dob, date_employed, role, address, salary)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, (name, email, gender, contact, dob, de, role, address, salary))
        self.conn.commit()
        self.fetch_data()
        messagebox.showinfo("Success", "Employee added successfully!")

    def fetch_data(self):
        self.cursor.execute("SELECT * FROM employees")
        rows = self.cursor.fetchall()

        # Clear existing rows in the table
        for row in self.EmployeeTable.get_children():
            self.EmployeeTable.delete(row)

        # Insert new rows into the table
        for row in rows:
            self.EmployeeTable.insert("", "end", values=row)

    def update_employee(self):
        selected_item = self.EmployeeTable.focus()  # Get selected item from the table
        if not selected_item:  # If no row is selected, show an error
                messagebox.showerror("Error", "Please select an employee to update!")
                return

        values = self.EmployeeTable.item(selected_item)["values"]  # Get the values of the selected row
        emp_id = values[0]  # Employee ID
        
        # Populate fields with the selected employee's details
        self.var_emp_id.set(emp_id)
        self.var_name.set(values[1])
        self.var_email.set(values[2])
        self.var_gender.set(values[3])
        self.var_contact.set(values[4])
        self.var_dob.set(values[5])
        self.var_de.set(values[6])
        self.var_role.set(values[7])
        self.var_salary.set(values[9])  # Salary is the 10th value
        self.txt_address.delete("1.0", "end-1c")  # Clear previous text
        self.txt_address.insert("1.0", values[8])  # Insert address into the address field

        # Now you can proceed with updating after validating the data
        name = self.var_name.get()
        email = self.var_email.get()
        gender = self.var_gender.get()
        contact = self.var_contact.get()
        dob = self.var_dob.get()
        de = self.var_de.get()
        role = self.var_role.get()
        salary = self.var_salary.get()
        address = self.txt_address.get("1.0", "end-1c")

        # Validate the data before updating
        error_message = self.validate_employee_data(name, email, gender, contact, dob, de, role, address, salary)
        if error_message:
                messagebox.showerror("Error", error_message)
                return

        # Update the employee record in the database
        self.cursor.execute(""" 
                UPDATE employees SET name=?, email=?, gender=?, contact=?, dob=?, date_employed=?, role=?, address=?, salary=? 
                WHERE emp_id=?
        """, (name, email, gender, contact, dob, de, role, address, salary, emp_id))
        self.conn.commit()  # Commit the transaction to the database
        self.fetch_data()  # Refresh the data in the table
        messagebox.showinfo("Success", "Employee details updated successfully!")

    def delete_employee(self):
        selected_item = self.EmployeeTable.focus()
        if not selected_item:
            messagebox.showerror("Error", "Please select an employee to delete!")
            return

        result = messagebox.askyesno("Confirm Delete", "Are you sure you want to delete this employee?")
        if result:  # If user clicked "Yes"
            values = self.EmployeeTable.item(selected_item)["values"]
            emp_id = values[0]

            self.cursor.execute("DELETE FROM employees WHERE emp_id=?", (emp_id,))
            self.conn.commit()

            self.EmployeeTable.delete(selected_item)
            messagebox.showinfo("Success", "Employee deleted successfully!")
        else:
            messagebox.showinfo("Cancelled", "Employee deletion cancelled.")

    def clear_fields(self):
        # Clear all input fields
        self.var_emp_id.set("")
        self.var_name.set("")
        self.var_email.set("")
        self.var_gender.set("Select")
        self.var_contact.set("")
        self.var_dob.set("")
        self.var_de.set("")
        self.var_role.set("Select")
        self.var_salary.set("")
        self.txt_address.delete("1.0", "end-1c")
        self.var_searchby.set("Select")
        self.var_searchtxt.set("")

    def search(self):
        search_by = self.var_searchby.get()
        search_txt = self.var_searchtxt.get()

        if search_by == "Select" or not search_txt:
            messagebox.showerror("Error", "Please select a search option and enter a search term.")
            return

        query = f"SELECT * FROM employees WHERE {search_by.lower()} LIKE ?"
        self.cursor.execute(query, ('%' + search_txt + '%',))
        rows = self.cursor.fetchall()

        for row in self.EmployeeTable.get_children():
            self.EmployeeTable.delete(row)

        for row in rows:
            self.EmployeeTable.insert("", "end", values=row)

    def close_window(self):
        self.conn.close()
        self.root.quit()

# Main function to run the application
def main():
    root = Tk()
    app = employeeClass(root)
    root.protocol("WM_DELETE_WINDOW", app.close_window)
    root.mainloop()

if __name__ == "__main__":
    main()