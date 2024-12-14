from tkinter import *
from tkinter import messagebox, ttk, filedialog
from PIL import Image, ImageTk  # Ensure Pillow library is installed
import json

class productClass:
    def __init__(self, root):
        self.root = root
        self.root.geometry('1310x650+208+182')  # Matching second file size and position
        self.root.title('Product/Stocks')
        self.root.configure(bg="#B9331C")
        self.root.focus_force()
        self.root.overrideredirect(1)

        # Inventory file paths
        self.inventory_file = "inventory.json"
        self.inventory = self.load_inventory()

        # Images directory
        self.images_dir = "product_images/"  # Ensure this folder exists
        self.product_images = self.load_product_images()

        # UI Components
        self.item_name_var = StringVar()
        self.stock_var = IntVar()
        self.price_var = DoubleVar()
        self.size_var = StringVar()

        Label(self.root, text="Item Name", font=("Verdana", 12), bg="#B9331C").place(x=50, y=50)
        Entry(self.root, textvariable=self.item_name_var, font=("Verdana", 12), bg="light yellow").place(x=200, y=50, width=200)

        Label(self.root, text="Stock Quantity", font=("Verdana", 12), bg="#B9331C").place(x=50, y=100)
        Entry(self.root, textvariable=self.stock_var, font=("Verdana", 12), bg="light yellow").place(x=200, y=100, width=200)

        Label(self.root, text="Price", font=("Verdana", 12), bg="#B9331C").place(x=50, y=150)
        Entry(self.root, textvariable=self.price_var, font=("Verdana", 12), bg="light yellow").place(x=200, y=150, width=200)

        Label(self.root, text="Size", font=("Verdana", 12), bg="#B9331C").place(x=50, y=200)

        # Size ComboBox
        self.size_combo = ttk.Combobox(self.root, textvariable=self.size_var, values=["Small", "Regular", "Large"], font=("Verdana", 12), state="readonly", height=3)
        self.size_combo.place(x=200, y=200, width=200)

        Button(self.root, text="Upload Image", font=("Verdana", 12), bg="purple", fg="white", command=self.upload_image).place(x=450, y=50, width=150)
        self.image_display = Label(self.root, text="No Image", bg="#B9331C", fg="white", font=("Verdana", 12))
        self.image_display.place(x=450, y=90, width=150, height=150)  # Adjusted Y position to place the image below the button

        Button(self.root, text="Add/Update Item", font=("Verdana", 12), bg="green", fg="white", command=self.add_update_stock).place(x=50, y=250, width=150)
        Button(self.root, text="Delete Item", font=("Verdana", 12), bg="red", fg="white", command=self.delete_item).place(x=250, y=250, width=150)
        Button(self.root, text="Edit Item", font=("Verdana", 12), bg="blue", fg="white", command=self.edit_item).place(x=450, y=250, width=150)

        # Display Current Inventory
        self.tree = ttk.Treeview(self.root, columns=("Item", "Stock", "Price", "Size"), show="headings", height=10)
        self.tree.heading("Item", text="Item")
        self.tree.heading("Stock", text="Stock")
        self.tree.heading("Price", text="Price")
        self.tree.heading("Size", text="Size")
        self.tree.column("Item", width=150)
        self.tree.column("Stock", width=100)
        self.tree.column("Price", width=100)
        self.tree.column("Size", width=100)
        self.tree.place(x=50, y=300, width=700, height=250)

        self.update_tree()

        # Bind select event for the tree
        self.tree.bind("<ButtonRelease-1>", self.select_item)

    def load_inventory(self):
        """Load inventory from a JSON file."""
        try:
            with open(self.inventory_file, "r") as file:
                return json.load(file)
        except FileNotFoundError:
            return {}

    def load_product_images(self):
        """Load product images information."""
        try:
            with open("product_images.json", "r") as file:
                return json.load(file)
        except FileNotFoundError:
            return {}

    def save_inventory(self):
        """Save the inventory to a JSON file."""
        with open(self.inventory_file, "w") as file:
            json.dump(self.inventory, file, indent=4)

    def save_product_images(self):
        """Save the product images to a JSON file."""
        with open("product_images.json", "w") as file:
            json.dump(self.product_images, file, indent=4)

    def add_update_stock(self):
        """Add or update an item."""
        item = self.item_name_var.get().strip()
        stock = self.stock_var.get()
        price = self.price_var.get()
        size = self.size_var.get().strip()

        if item == "" or stock < 0 or price < 0 or size == "":
            messagebox.showerror("Error", "Please provide valid item details.")
            return

        # Update inventory or add new item
        if item in self.inventory:
            self.inventory[item]["stock"] += stock  # Update stock for existing item
        else:
            self.inventory[item] = {
                "stock": stock,
                "price": price,
                "size": size,
            }

        self.save_inventory()

        if item not in self.product_images:
            self.product_images[item] = None  # Initialize image association if not already
        self.save_product_images()

        messagebox.showinfo("Success", f"Item '{item}' added/updated.")
        self.clear_fields()
        self.update_tree()

    def delete_item(self):
        """Delete an item from the inventory."""
        item = self.item_name_var.get().strip()

        if item == "":
            messagebox.showerror("Error", "Please select an item to delete.")
            return

        if item in self.inventory:
            del self.inventory[item]
            if item in self.product_images:
                del self.product_images[item]
                self.save_product_images()

            self.save_inventory()
            messagebox.showinfo("Success", f"Item '{item}' has been deleted.")
            self.clear_fields()
            self.update_tree()
        else:
            messagebox.showerror("Error", f"Item '{item}' not found.")

    def edit_item(self):
        """Edit the stock, price, or size of an existing item."""
        item = self.item_name_var.get().strip()
        stock = self.stock_var.get()
        price = self.price_var.get()
        size = self.size_var.get().strip()

        if item == "" or stock < 0 or price < 0 or size == "":
            messagebox.showerror("Error", "Please provide valid item details.")
            return

        if item in self.inventory:
            self.inventory[item] = {"stock": stock, "price": price, "size": size}
            self.save_inventory()
            messagebox.showinfo("Success", f"Item '{item}' has been updated.")
            self.clear_fields()
            self.update_tree()
        else:
            messagebox.showerror("Error", f"Item '{item}' not found.")

    def upload_image(self):
        """Upload an image for a product."""
        item = self.item_name_var.get().strip()

        if not item:
            messagebox.showerror("Error", "Please enter a product name first.")
            return

        file_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.png;*.jpg;*.jpeg")])
        if file_path:
            self.product_images[item] = file_path
            self.save_product_images()
            self.display_image(file_path)

    def display_image(self, file_path):
        """Display the product image."""
        try:
            img = Image.open(file_path)
            img = img.resize((150, 150), Image.Resampling.LANCZOS)
            img = ImageTk.PhotoImage(img)
            self.image_display.config(image=img, text="")  # Display the image
            self.image_display.image = img  # Keep a reference to prevent garbage collection
        except Exception as e:
            messagebox.showerror("Error", f"Could not display image: {str(e)}")

    def update_tree(self):
        """Update the inventory table."""
        for item in self.tree.get_children():
            self.tree.delete(item)
        for key, value in self.inventory.items():
            self.tree.insert("", "end", values=(key, value["stock"], value["price"], value["size"]))

    def select_item(self, event):
        """Select an item from the table."""
        selected = self.tree.focus()
        values = self.tree.item(selected, "values")

        if values:
            self.item_name_var.set(values[0])
            self.stock_var.set(values[1])
            self.price_var.set(values[2])
            self.size_var.set(values[3])

            # Get the image path for the selected item
            if values[0] in self.product_images and self.product_images[values[0]]:
                product_image_path = self.product_images[values[0]]
            else:
                product_image_path = None

            # Pass the image path to the ordering system
            self.ordering_system.show_selected_product_image(product_image_path)

    def clear_fields(self):
        """Clear input fields."""
        self.item_name_var.set("")
        self.stock_var.set(0)
        self.price_var.set(0.0)
        self.size_var.set("")

    def update_inventory(self, item, quantity):
        """Update inventory when an order is placed."""
        if item in self.inventory:
            self.inventory[item]["stock"] -= quantity
            self.save_inventory()
            self.update_tree()
        else:
            print(f"Item '{item}' not found in inventory.")

    def clear_fields(self):
        """Clear input fields."""
        self.item_name_var.set("")
        self.stock_var.set(0)
        self.price_var.set(0.0)
        self.size_var.set("")

if __name__ == "__main__":
    root = Tk()
    obj = productClass(root)
    root.mainloop()
