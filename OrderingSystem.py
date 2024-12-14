import json
import time
from tkinter import *
from datetime import datetime
from PIL import Image, ImageTk
from tkinter import messagebox, ttk

class OrderingSystem:
    def confirm_exit(self):
        """Prompt the user to confirm the 'exit' action."""
        result = messagebox.askyesno("Exit", "Are you sure you want to exit? Your order will not be saved.")
        if result:  # If 'Yes' is clicked
            self.root.quit()  # Close the window

    def __init__(self, root):
        self.root = root
        self.root.title("Customer Ordering System")
        self.root.geometry('1500x820')
        self.root.resizable(0, 0)
        self.root.configure(bg="#B9331C")
        self.root.overrideredirect(1)

        # Center the window
        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()
        x_coordinate = (screen_width // 2) - (1500 // 2)
        y_coordinate = (screen_height // 2) - (820 // 2)
        root.geometry(f'1500x820+{x_coordinate}+{y_coordinate}')


        # Title bar
        title_bar = Frame(self.root, bg="#B9331C", relief=RAISED, height=30)
        title_bar.pack(side=TOP, fill=X)
        title_label = Label(title_bar, text="Ordering System", bg="#B9331C", fg="white", font=("Arial", 12, "bold"))
        title_label.pack(side=LEFT, padx=10)


        close_btn = Button(title_bar, text="X", font=("Verdana", 10, "bold"), bg="red", fg="white", border=0, cursor="hand2", command=self.confirm_exit)
        close_btn.pack(side=RIGHT, padx=5, pady=2)
    
        # Inventory file path
        self.inventory_file = "inventory.json"
        self.inventory = self.load_inventory()
        self.orders = []  # Store customer orders

        # Navigation panel
        self.navigation_panel = Frame(self.root, bg="#B9331C", width=200, relief=RAISED)
        self.navigation_panel.pack(side=LEFT, fill=Y)
        self.create_navigation_buttons()

        # Main content frame
        self.main_content = Frame(self.root, bg="#B9331C", relief=RAISED)
        self.main_content.place(x=227, y=39, relwidth=0.87, relheight=0.97)

        # Initialize frames for each section
        self.init_ordering_section()
        self.init_customer_details_section()
        self.init_summary_section()

        self.show_ordering_section()  # Default view

    # Clock showing Date and Time
        self.clock = Label(self.root, text="Welcome to Pyzzahut! Date: DD-MM-YYYY Time: HH:MM:SS", font=("Verdana", 15), bg="black", fg="white")
        self.clock.place(x=0, y=115, relwidth=1, height=30)
        self.update_clock()


    def update_clock(self):
        """ Update the clock every second. """
        current_time = time.strftime('%H:%M:%S')
        current_date = time.strftime('%d-%m-%Y')
        self.clock.config(text=f"Welcome to Pyzzahut!  Date: {current_date}  Time: {current_time}")
        self.clock.after(1000, self.update_clock)

    def create_navigation_buttons(self):
        """Create navigation buttons."""
        Button(self.navigation_panel, text="Ordering", font=("Verdana", 12, "bold"), bg="Peru", fg="white",activebackground="Peru",command=self.show_ordering_section, height=3, width=20).place(y=120)
        Button(self.navigation_panel, text="Customer Details", font=("Verdana", 12, "bold"), bg="Peru", fg="white",activebackground="Peru",command=self.show_customer_details_section, height=3, width=20).place(y=200)
        Button(self.navigation_panel, text="Summary", font=("Verdana", 12, "bold"), bg="Peru", fg="white",activebackground="Peru",command=self.show_summary_section, height=3, width=20).place(y=280)
    
    def load_inventory(self):
        """Load inventory from a JSON file."""
        try:
            with open(self.inventory_file, "r") as file:
                return json.load(file)
        except FileNotFoundError:
            messagebox.showerror("Error", "Inventory file not found. Please contact admin.")
            return {}

    def save_inventory(self):
        """Save the inventory to a JSON file."""
        with open(self.inventory_file, "w") as file:
            json.dump(self.inventory, file, indent=4)

    def update_item_list(self):
        """Update the item dropdown list."""
        self.item_combo["values"] = list(self.inventory.keys())

    def init_ordering_section(self):
        try:
            # Open the image using PIL
            image = Image.open("Menu.png")  # Replace with your image path

            # Convert the image to Tkinter-compatible format
            tk_image = ImageTk.PhotoImage(image)

            # Create a label widget to display the image
            menu_label = Label(self.main_content, image=tk_image)
            menu_label.image = tk_image  # Keep a reference to the image
            menu_label.place(x=50, y=-60, width=1250, height=510)  # Adjust position and size as needed

        except Exception as e:
            print(f"An error occurred: {e}")
            Label(self.main_content, text="Error loading menu image", font=("Verdana", 12), bg="white", fg="red").place(x=50, y=50)

        # Load background image for the entire window
            self.bg_image = Image.open("Ordering.png")  # Replace with your background image path
            self.bg_image = self.bg_image.resize((1500, 820), Image.ANTIALIAS)  # Resize to fit window size
            self.bg_image_tk = ImageTk.PhotoImage(self.bg_image)  # Convert to Tkinter-compatible format

        # Set background label without affecting other elements
            bg_label = Label(self.root, image=self.bg_image_tk)
            bg_label.image = self.bg_image_tk  # Keep a reference to the image
            bg_label.place(x=0, y=0)  # Adjust size and position to fit the window

        """Create UI for the Ordering section."""
        Label(self.main_content, text="Select Item", font=("Verdana", 12,"bold"), bg="white").place(x=50, y=350)
        self.item_name_var = StringVar()
        self.item_combo = ttk.Combobox(self.main_content, textvariable=self.item_name_var, font=("Verdana", 12), state="readonly")
        self.item_combo.place(x=170, y=350, width=200)
        self.update_item_list()

        Label(self.main_content, text="Quantity", font=("Verdana", 12,"bold"), bg="#B9331C").place(x=50, y=400)
        self.quantity_var = IntVar()
        Entry(self.main_content, textvariable=self.quantity_var, font=("Verdana", 12), bg="light yellow").place(x=170, y=400, width=200)

        Label(self.main_content, text="Size", font=("Verdana", 12,"bold"), bg="#B9331C").place(x=50, y=300)
        self.size_var = StringVar()
        self.size_combo = ttk.Combobox(self.main_content, textvariable=self.size_var, font=("Verdana", 12), state="readonly")
        self.size_combo["values"] = ["Small", "Regular", "Large"]
        self.size_combo.place(x=170, y=300, width=200)
        self.size_combo.set("Regular")

        Label(self.main_content, text="Select Item", font=("Verdana", 12,"bold"), bg="#B9331C").place(x=50, y=350)
        self.item_name_var = StringVar()
        self.item_combo = ttk.Combobox(self.main_content, textvariable=self.item_name_var, font=("Verdana", 12), state="readonly")
        self.item_combo.place(x=170, y=350, width=200)
        self.update_item_list()

        Label(self.main_content, text="Quantity", font=("Verdana", 12,"bold"), bg="#B9331C").place(x=50, y=400)
        self.quantity_var = IntVar()
        Entry(self.main_content, textvariable=self.quantity_var, font=("Verdana", 12), bg="light yellow").place(x=170, y=400, width=200)

        Button(self.main_content, text="Add Order", font=("Verdana", 12), bg="green", fg="white", command=self.add_order).place(x=50, y=450, width=100)
        Button(self.main_content, text="Edit Order", font=("Verdana", 12), bg="orange", fg="white", command=self.edit_order).place(x=160, y=450, width=100)
        Button(self.main_content, text="Delete Order", font=("Verdana", 12), bg="red", fg="white", command=self.delete_order).place(x=270, y=450, width=100)

        self.order_listbox = Listbox(self.main_content, font=("Verdana", 12), bg="light yellow", height=10, width=50)
        self.order_listbox.place(x=50, y=500)

        self.total_price_label = Label(self.main_content, text="Total Price: ₱0", font=("Verdana", 14, "bold"), bg="#B9331C")
        self.total_price_label.place(x=50, y=700)

    def place_order(self):
        item = self.item_name_var.get()
        quantity = self.quantity_var.get()

        if item == "" or quantity <= 0:
                messagebox.showerror("Error", "Please provide valid order details.")
                return

        if item not in self.inventory:
                messagebox.showerror("Error", f"Item '{item}' not found in inventory.")
        elif self.inventory[item]["stock"] < quantity:
                messagebox.showerror("Error", f"Insufficient stock for '{item}'. Only {self.inventory[item]['stock']} units available.")
        else:
                # Deduct stock
                self.inventory[item]["stock"] -= quantity
                self.save_inventory()
                self.product_class.update_inventory(item, quantity)  # Update productClass inventory

                messagebox.showinfo("Success", f"Order placed for {quantity} units of '{item}'.")
                self.update_item_list()
                self.quantity_var.set(0)
    def update_inventory(self, item, quantity):
        """Update inventory when an order is placed."""
        print(f"Before update: {self.inventory}")
        if item in self.inventory:
            self.inventory[item]["stock"] -= quantity
            self.save_inventory()
            self.update_tree()
            print(f"After update: {self.inventory}")
        else:
            print(f"Item '{item}' not found in inventory.")

    def init_customer_details_section(self):
        """Create UI for the Customer Details section."""
        Label(self.main_content, text="Customer Details", font=("Verdana", 20, "bold"), bg="#B9331C").place(x=400,y=130)
        self.customer_name_var = StringVar()
        Label(self.main_content, text="Name", font=("Verdana", 12,"bold"), bg="#B9331C").place(x=350, y=180)
        Entry(self.main_content, textvariable=self.customer_name_var, font=("Verdana", 12,"bold"), bg="light yellow").place(x=450, y=180, width=300)
        self.customer_contact_var = StringVar()
        Label(self.main_content, text="Contact", font=("Verdana", 12,"bold"), bg="#B9331C").place(x=350, y=220)
        Entry(self.main_content, textvariable=self.customer_contact_var, font=("Verdana", 12), bg="light yellow").place(x=450, y=220, width=300)
        self.customer_email_var = StringVar()
        Label(self.main_content, text="Email", font=("Verdana", 12,"bold"), bg="#B9331C").place(x=350, y=260)
        Entry(self.main_content, textvariable=self.customer_email_var, font=("Verdana", 12), bg="light yellow").place(x=450, y=260, width=300)
        self.customer_address_var = StringVar()
        Label(self.main_content, text="Address", font=("Verdana", 12,"bold"), bg="#B9331C").place(x=350, y=300)
        Entry(self.main_content, textvariable=self.customer_address_var, font=("Verdana", 12), bg="light yellow").place(x=450,y=300, width=300)
        Button(self.main_content, text="Save Details", font=("Verdana", 12), bg="green", fg="white", command=self.save_order_summary).place(x=530, y=340)

    def save_order_summary(self):
        """Save the order summary to a sales file."""
        if not self.orders:
            messagebox.showerror("Error", "No orders to save.")
            return

        customer_data = {
            "name": self.customer_name_var.get(),
            "contact": self.customer_contact_var.get(),
            "email": self.customer_email_var.get(),
            "address": self.customer_address_var.get(),
            "orders": self.orders,
            "total_price": sum(order["quantity"] * order["price"] for order in self.orders),
            "date_time": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }

        if not all(customer_data.values()):
            messagebox.showerror("Error", "Please fill in all customer details before saving.")
            return

        try:
            # Append order details to the sales.json file
            sales_file = "sales.json"
            try:
                with open(sales_file, "r") as file:
                    sales_data = json.load(file)
            except FileNotFoundError:
                sales_data = []

            sales_data.append(customer_data)

            with open(sales_file, "w") as file:
                json.dump(sales_data, file, indent=4)

            messagebox.showinfo("Success", "Order summary saved successfully.")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to save summary: {e}")

    def init_summary_section(self):
        """Create UI for the Summary section."""
        Label(self.main_content, text="Order Summary", font=("Verdana", 20, "bold"), bg="#B9331C").pack(pady=130)
        self.summary_text = Text(self.main_content, font=("Verdana", 12), bg="light yellow")
        self.summary_text.place(x=310, y=185, width=600, height=400)

        # Add Done button
        Button(self.main_content, text="Done", font=("Verdana", 12), bg="green", fg="white", command=self.confirm_done).place(x=600, y=600)

    def confirm_done(self):
        """Prompt the user to confirm the 'Done' action only if there is a selected order."""
        # Check if there is any content in the summary text (i.e., if an order is placed)
        if not self.summary_text.get("1.0", "end-1c").strip():
            messagebox.showwarning("No Order", "Please select at least one item before finishing your order.")
            return  # Exit the method if no order has been selected

    # If there is content (i.e., order is selected), ask for confirmation
        result = messagebox.askyesno("Confirm Done", "Are you sure you are done with your order?")
        if result:  # If Yes is clicked
            messagebox.showinfo("Thank You", "Thank you for ordering! Happy eating!")
        self.root.quit()  # Close the window

    def confirm_logout(self):
        """Prompt the user to confirm logout action."""
        result = messagebox.askyesno("Confirm Logout", "Are you sure? Your order will be discarded.")
        if result:  # If Yes is clicked
            self.root.quit()  # Close the window


    def show_ordering_section(self):
        """Show the Ordering section."""
        self.clear_main_content()
        self.init_ordering_section()

    def show_customer_details_section(self):
        """Show the Customer Details section."""
        self.clear_main_content()
        self.init_customer_details_section()

    def show_summary_section(self):
        """Show the Summary section."""
        self.clear_main_content()
        self.init_summary_section()

        # Display customer details in the summary
        self.summary_text.insert(END, f"Customer Name: {self.customer_name_var.get()}\n")
        self.summary_text.insert(END, f"Contact: {self.customer_contact_var.get()}\n")
        self.summary_text.insert(END, f"Email: {self.customer_email_var.get()}\n")
        self.summary_text.insert(END, f"Address: {self.customer_address_var.get()}\n")

        # Display the list of ordered items
        self.summary_text.insert(END, "Orders:\n")
        total_price = 0
        for order in self.orders:
                item_name = order["item"]
                quantity = order["quantity"]
                price = order["price"]
                item_price = quantity * price
                total_price += item_price
                self.summary_text.insert(END, f"- {item_name} ({order['size']}) x{quantity} (₱{item_price})\n")
        
        # Display total price
        self.summary_text.insert(END, f"Total Price: ₱{total_price}\n")


    def clear_main_content(self):
        """Clear all widgets from the main content area."""
        for widget in self.main_content.winfo_children():
            widget.destroy()

    def add_order(self):
        item = self.item_name_var.get().strip()
        size = self.size_combo.get().lower()  # Ensure the size is lowercase
        quantity = self.quantity_var.get()

        if item == "" or quantity <= 0:
            messagebox.showerror("Error", "Please provide valid order details.")
            return

        if item not in self.inventory:
            messagebox.showerror("Error", f"Item '{item}' not found in inventory.")
            return

        # Check if the selected size matches the inventory size
        inventory_item = self.inventory[item]
        if inventory_item["size"].lower() != size:
            messagebox.showerror("Error", f"Size '{size}' not available for '{item}'. Available size: '{inventory_item['size']}'.")
            return

        if inventory_item["stock"] < quantity:
            messagebox.showerror("Error", f"Insufficient stock for '{item}' size '{size}'.")
            return

        # Get the price from the inventory for the specific item
        price = inventory_item["price"]
    
        # Add the order to the orders list
        self.orders.append({"item": item, "size": size, "quantity": quantity, "price": price})
    
        # Update the stock and the order list box
        self.inventory[item]["stock"] -= quantity
        self.order_listbox.insert(END, f"{item} ({size}) x{quantity}")
    
        # Update total price and show success message
        self.update_total_price()
        messagebox.showinfo("Success", f"Added {quantity} {size} {item}(s) to orders.")


    def edit_order(self):
        """Edit the selected order."""
        selected_index = self.order_listbox.curselection()
        if not selected_index:
            messagebox.showerror("Error", "Please select an order to edit.")
            return
        index = selected_index[0]
        old_order = self.orders[index]

        # Return stock to inventory before editing
        self.inventory[old_order["item"]]["stock"] += old_order["quantity"]

        # Update with new order details
        item = self.item_name_var.get()
        quantity = self.quantity_var.get()
        if item not in self.inventory or quantity <= 0:
            messagebox.showerror("Error", "Invalid order details.")
            return

        if self.inventory[item]["stock"] < quantity:
            messagebox.showerror("Error", f"Insufficient stock for '{item}'.")
            return

        self.orders[index] = {"item": item, "quantity": quantity}
        self.inventory[item]["stock"] -= quantity
        self.order_listbox.delete(index)
        self.order_listbox.insert(index, f"{item} x{quantity}")
        self.update_total_price()
        messagebox.showinfo("Success", "Order updated.")

    def delete_order(self):
        """Delete the selected order."""
        selected_index = self.order_listbox.curselection()
        if not selected_index:
            messagebox.showerror("Error", "Please select an order to delete.")
            return
        index = selected_index[0]
        order = self.orders.pop(index)

        # Return stock to inventory
        self.inventory[order["item"]]["stock"] += order["quantity"]
        self.order_listbox.delete(index)
        self.update_total_price()
        messagebox.showinfo("Success", "Order deleted.")

    def update_total_price(self):
        """Update the total price label."""
        total_price = sum(order["quantity"] * self.inventory[order["item"]]["price"] for order in self.orders)
        self.total_price_label.config(text=f"Total Price: ₱{total_price}")

if __name__ == "__main__":
    root = Tk()
    app = OrderingSystem(root)
    root.mainloop()
