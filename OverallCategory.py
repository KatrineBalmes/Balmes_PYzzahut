from tkinter import *

class overallClass:
    def __init__(self, root):
        self.root = root
        self.root.geometry('1310x650+208+182')
        self.root.title('Overall Category')
        self.root.configure(bg="#B9331C")
        self.root.focus_force()
        self.root.overrideredirect(1)

        def close_app():
            root.destroy()

        # Custom title bar
        title_bar = Frame(self.root, bg="brown", relief=RAISED, height=30)
        title_bar.pack(side=TOP, fill=X)
        title_label = Label(title_bar, text="Overall Category", font=("Verdana", 18, "bold"), bg="brown", fg="white")
        title_label.pack(side=LEFT, padx=10)

        # Employee Frame
        self.emp_frame = Frame(self.root, bg="peru", border=3, relief=RIDGE)
        self.emp_frame.place(x=200, y=200, height=300, width=300)

        self.total_emp_logo = self.load_image("LogoEmp.png")  # Load the logo
        if self.total_emp_logo:
            self.total_emp_logo_label_name = Label(text="Total Employee\n[0]", bg="peru", font=('Verdana', 15, 'bold'))
            self.total_emp_logo_label_name.place(x=268, y=388)
            self.total_emp_logo_label = Label(self.emp_frame, border=0, image=self.total_emp_logo)
            self.total_emp_logo_label.pack()

        # Product Frame
        self.product_frame = Frame(self.root, bg="peru", border=3, relief=RIDGE)
        self.product_frame.place(x=550, y=200, height=300, width=300)

        self.total_prod_logo = self.load_image("LogoProd.png")  # Load the logo
        if self.total_prod_logo:
            self.total_prod_logo_label_name = Label(text="Total Stocks\n[0]", bg="peru", font=('Verdana', 15, 'bold'))
            self.total_prod_logo_label_name.place(x=635, y=390)
            self.total_prod_logo_label = Label(self.product_frame, border=0, image=self.total_prod_logo)
            self.total_prod_logo_label.pack()

        # Sales Frame
        self.sales_frame = Frame(self.root, bg="peru", border=3, relief=RIDGE)
        self.sales_frame.place(x=900, y=200, height=300, width=300)

        self.total_sales_logo = self.load_image("LogoSales.png")  # Load the logo
        if self.total_sales_logo:
            self.total_sales_logo_label_name = Label(text="Total Sales\n[0]", bg="peru", font=('Verdana', 15, 'bold'))
            self.total_sales_logo_label_name.place(x=979, y=390)
            self.total_sales_logo_label = Label(self.sales_frame, border=0, image=self.total_sales_logo)
            self.total_sales_logo_label.pack()
        
    def load_image(self, filepath):
        """ Attempt to load an image and handle exceptions. """
        try:
            return PhotoImage(file=filepath)
        except Exception as e:
            print(f"Error loading image '{filepath}': {e}")
            return None

if __name__ == "__main__":
    root = Tk()
    obj = overallClass(root)
    root.mainloop()