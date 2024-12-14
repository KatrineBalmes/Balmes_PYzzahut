from tkinter import *
import subprocess

class WelcomePage:
    def __init__(self, root):
        self.root = root
        self.root.geometry('1500x820')
        self.root.title('Welcome Page')
        self.root.resizable(0, 0)
        self.root.configure(bg="brown")
        self.root.overrideredirect(1)  # Removes default window decorations

        # Center the window on the screen
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        x_coordinate = (screen_width // 2) - (1500 // 2)  # Center horizontally
        y_coordinate = (screen_height // 2) - (820 // 2)  # Center vertically
        self.root.geometry(f'1500x820+{x_coordinate}+{y_coordinate}')

        # Title bar
        title_bar = Frame(self.root, bg="brown", relief=RAISED, height=30)
        title_bar.pack(side=TOP, fill=X)

        # Close button
        close_btn = Button(title_bar, text="X", font=("Verdana", 10, "bold"), bg="red", fg="white",border=0, cursor="hand2", command=self.root.destroy)
        close_btn.pack(side=RIGHT, padx=5, pady=2)

        # Title label
        title_label = Label(title_bar, text="Welcome Page", font=("Verdana", 14, "bold"), bg="brown", fg="white")
        title_label.pack(side=LEFT, padx=10)

        # Background image 
        self.background_image = PhotoImage(file='WelcomeBackground.png')
        background_label = Label(self.root, image=self.background_image, bg='brown')
        background_label.place(x=0, y=30)  # Adjusted y to place below the title bar

        # "Order Now" Button
        order_btn = Button(self.root, text="Register Now!", font=("Verdana", 14, "bold"), bg="peru", fg="white",cursor="hand2", border=0, command=self.open_order_window)
        order_btn.place(x=1220, y=700, width=200, height=50)


    def open_order_window(self):
        order_window = Toplevel(self.root)
        order_window.geometry(self.root.geometry())
        order_window.configure(bg="brown")
        order_window.resizable(0, 0)
        
        order_window.overrideredirect(1)

        # Title bar
        title_bar = Frame(order_window, bg="#B9331C", relief="raised", height=30)
        title_bar.pack(side=TOP, fill=X)

        # Close button
        close_btn = Button(title_bar, text="X", font=("Verdana", 10, "bold"), bg="red", fg="white",
        border=0, cursor="hand2", command=order_window.destroy)
        close_btn.pack(side=RIGHT, padx=5, pady=2)
        
        # Background image (same as the main window, stretch to cover entire popup)
        self.background_image_popup = PhotoImage(file='AdminCustomerBg.png')  # Keep a reference here
        background_label_popup = Label(order_window, image=self.background_image_popup, bg='brown')
        background_label_popup.place(x=0, y=30)  # Stretch to cover the entire window

        # Button 1 with image as background
        try:
                self.button_image_1 = PhotoImage(file='admin.png')  # Add your button image path
                button_1 = Button(order_window,image=self.button_image_1, border=0, bg="brown",cursor='hand2',activebackground="#B9331C",command=self.order_button_1_action)
                button_1.place(x=800, y=300)  # Position the button

                # Add Admin label
                admin_label = Label(order_window, text="Admin", font=("Verdana", 12, "bold"), bg="#B9331C", fg="white")
                admin_label.place(x=880, y=470)  # Adjust position below the button
        except Exception as e:
                print(f"Error loading button 1 image: {e}")
        
        # Button 2 with image as background
        try:
                self.button_image_2 = PhotoImage(file='customer.png')  # Add your button image path
                button_2 = Button(order_window, image=self.button_image_2, border=0,bg="brown",cursor='hand2',activebackground="#B9331C",command=self.order_button_2_action)
                button_2.place(x=1100, y=300)  # Position the second button

                # Add Customer label
                customer_label = Label(order_window, text="Customer", font=("Verdana", 12, "bold"), bg="#B9331C", fg="white")
                customer_label.place(x=1165, y=470) 
        except Exception as e:
                print(f"Error loading button 2 image: {e}")


    def order_button_1_action(self):
        subprocess.Popen(["python", "AdminLogin.py"])
        root.destroy()

    def order_button_2_action(self):
        subprocess.Popen(["python", "CustomerLogin.py"])
        root.destroy()

if __name__ == "__main__":
    root = Tk()
    welcome_page = WelcomePage(root)
    root.mainloop()
