# Balmes_PYzzahut
Welcome to Balmes_Final Project in Advance Computer Programming entitled "PYzzahut" crafted by Katrine Angeleen Balmes. This repository is a guidance which involves README file that stands ready to narrate the project's overview and its alignment in  SDG's. 
## Overview 
The PYzzahut system is designed to provide an efficient ordering process for customers while ensuring effective inventory management for administrators.The PYzzahut system is designed to track inventory and sales management. One of its main functions is inventory management, which records product information like price, size, while monitoring and updating stock levels. By connecting order placing to sales tracking and keeping track of the total amount of orders, it also makes sales management easier. 
## Python Tkinter applied:
## 1. from tkinter import *:
- This import brings in all the classes and functions from the tkinter library, which is essential for the creator to create the graphical user interface (GUI) of the project. 
## 2. import subprocess:
- This import allows  to spawn new processes and interact with them.
## 3. import time:
- This library helps to manage time-related functions. In this project, It is used  to update and display the current time every second (self.update_clock()), keeping the clock visible and updated in real-time on the interface.
## 4. from datetime import datetime:
- In PYxxahut system it is used  to retrieve the current date and time, which is essential when checking and managing the exact time of a customer's order.
## 5. from PIL import Image, ImageTk:
-  Image lets the creator to open and manipulate images (such as resizing them), and ImageTk converts them into a format that Tkinter can display.
## 6. from tkinter import messagebox:
- This import allows  to use message boxes to show pop-up messages to the user, like alerts, confirmations, or errors. In PYzzahut this more use when an orders is successfully added or when an error occurs.
## 7.import re: 
- The re library allows me to use regular expressions, which help with advanced string matching and manipulation.
## SQLITE 3
- The PYzzahut is not totally all managed by MySQL. Though sqlite3 is easy to apply or use due to it can be installed in extension only beacuse it is part of Python's standard library.
## JSON
- Since the creator  encountered some challenges with using sqlite3 for tracking the product and inventory in my program, so the creator decided to look for an alternative way to store and manage the data. JSON can easily read and write data in the lightweight JSON format.
## Sustainable Development Goals Applied:
## SDG 12: Responsible Consumption and Production
-  PYzzahut supports SDG 12 in a way of this system can be a big help in minimizing food waste because of it tracks stock so this strategy not only reduces needless waste but also helps firms save money and become more profitable
## SDG 3: Good Health and Well-being
- By focusing on reducing food waste and promoting sustainable resource usage, Pyzzahut indirectly contributes to this goal in several ways.
## Instruction on running the code
1. Install Python 3.8 or up
2.Install the following libraries in the command prompt, this is for handling and displaying images (pip install pillow)
3. Ensure you have the image files used in the system
4.Navigate to the program (folder) containing  the program files
5.Run the program
## PROGRAM
##  Welcome Page
##  Choose Login: Login as Customer or Login as a Admin
##  Login as a Admin
Insert Username (admin) and Pyzzword (Pyzzword)
## Dashboard
4 button Overall Category, Employee, Product/Stocks, Sales
## Overall Category
Just a Display
## Employee
1. Save -The admin need to fill up all the needed details, then once you clicked save it will automatically display on the table
2. Update - The admin must clicked first the row in the table that they want to update after that they need to save and just delete the data they don’t need
3. Delete -  The admin must select the row in the table they want to delete, and then there will prompt pop making sure that they totally want to delete that row.
4. Clear - All the input entry details will be clear/ disappear.
 ## Produc/Stock Dashboard
- The user can ass, update, delete stock, upload product iteml also the price, can also upload picture. This is connected to OrderingClass.
## Sales Dashboard
- Sales Dashboard is also connected to the Ordering System where all the customer ordered in the ordering sytem are listed here including their name, contact, address, orders, total price and the date & time when they ordered.
## Click Signing in
Signing in up the customer already have account.
## Click Signing up
If the customer doesn't have account iin this ordering system. Make sure to fill all of the information because the user can’t sign-up if there are missing details. Also don’t’ forget to clicked the “I agree to the terms and conditions.
## Ordering System
## Click in 3 Navigation Panel Button
## 1. Ordering
Select item the customer wants. If the customer selects an item that is unavailable, a message box will appear displaying the available sizes for their chosen item.
## 2. Customer Details 
Provide all the details, then once the user clicked the save details. Their information will save in summary also in the Sales Dashboard.'
## 3. Summary of the Order
All the information of the customer, their order and the total price of their order will show up here.
# Click Exit
End of the Program.
