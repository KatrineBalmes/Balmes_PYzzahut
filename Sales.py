import json
from tkinter import *
from tkinter import ttk
from tkinter import messagebox

class salesClass:
    def __init__(self, root):
        self.root = root
        self.root.geometry('1310x650+208+182')
        self.root.title('Sales')
        self.root.configure(bg="#B9331C")
        self.root.focus_force()
        self.root.overrideredirect(1)

        title_bar = Frame(root, bg="#B9331C", relief="raised", height=30)
        title_bar.pack(side=TOP, fill=X)
        title_label = Label(title_bar, text="Sales", bg="#B9331C", fg="white", font=("Arial", 12, "bold"))
        title_label.pack(side=LEFT, padx=10)

        # Title
        Label(self.root, text="Sales Records", font=("Arial", 18, "bold"), bg="#B9331C", fg="white").pack(fill=X)

        # Table Frame
        table_frame = Frame(self.root)
        table_frame.pack(fill=BOTH, expand=True, padx=10, pady=10)

        # Sales Table
        self.sales_table = ttk.Treeview(table_frame, columns=("Name", "Contact", "Email", "Address", "Orders", "Total Price", "Date & Time"), show="headings")
        self.sales_table.heading("Name", text="Customer Name")
        self.sales_table.heading("Contact", text="Contact")
        self.sales_table.heading("Email", text="Email")
        self.sales_table.heading("Address", text="Address")
        self.sales_table.heading("Orders", text="Orders")
        self.sales_table.heading("Total Price", text="Total Price (₱)")
        self.sales_table.heading("Date & Time", text="Date & Time")
        self.sales_table.column("Name", width=150)
        self.sales_table.column("Contact", width=100)
        self.sales_table.column("Email", width=150)
        self.sales_table.column("Address", width=200)
        self.sales_table.column("Orders", width=300)
        self.sales_table.column("Total Price", width=100)
        self.sales_table.column("Date & Time", width=150)

        self.sales_table.pack(fill=BOTH, expand=True)

        # Add Delete Button
        delete_button = Button(self.root, text="Delete Selected Record", font=("Arial", 12), bg="red", fg="white", command=self.delete_selected_record)
        delete_button.pack(pady=10)

        # Load Sales Data
        self.load_sales_data()

    def load_sales_data(self):
        """Load sales data from the sales.json file."""
        sales_file = "sales.json"
        try:
            with open(sales_file, "r") as file:
                sales_data = json.load(file)
            for record in sales_data:
                orders_summary = "\n".join([f"{order['item']} x{order['quantity']} ({order['size']})" for order in record["orders"]])
                self.sales_table.insert("", END, values=(
                    record["name"],
                    record["contact"],
                    record["email"],
                    record["address"],
                    orders_summary,
                    f"₱{record['total_price']}",
                    record["date_time"]
                ))
        except FileNotFoundError:
            messagebox.showerror("Error", "No sales data found. Please save some orders first.")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to load sales data: {e}")

    def delete_selected_record(self):
        """Delete the selected record from the table and JSON file."""
        selected_item = self.sales_table.selection()
        if not selected_item:
            messagebox.showwarning("No Selection", "Please select a record to delete.")
            return
        
        # Ask for confirmation
        confirm = messagebox.askyesno("Confirm Delete", "Are you sure you want to delete the selected record?")
        if confirm:
            # Get the selected record index
            selected_record = self.sales_table.item(selected_item[0])
            record_values = selected_record['values']
            customer_name = record_values[0]  # Assuming 'Name' is the first column

            # Load existing sales data
            sales_file = "sales.json"
            try:
                with open(sales_file, "r") as file:
                    sales_data = json.load(file)

                # Remove the record with matching customer name
                sales_data = [record for record in sales_data if record["name"] != customer_name]

                # Save the updated sales data back to the file
                with open(sales_file, "w") as file:
                    json.dump(sales_data, file, indent=4)

                # Remove the record from the table
                self.sales_table.delete(selected_item[0])

                messagebox.showinfo("Success", f"Record for {customer_name} has been deleted.")
            except Exception as e:
                messagebox.showerror("Error", f"Failed to delete the record: {e}")

if __name__ == "__main__":
    root = Tk()
    obj = salesClass(root)
    root.mainloop()
