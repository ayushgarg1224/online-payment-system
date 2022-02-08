“Online Payment System”
The project is aimed at replicating an online payment system. It allows its user to place an order to an online retail shop designed for the purpose of the program. It starts by presenting an entry box for the user to enter the name of the watch they wish to purchase while specifying the quantity. The program then checks the availability of the entered product and verifies the stock from a MySQL table. If the product is available in the required amount, the program then presents the user with an entry box to enter their banking information. It takes in their CVV, date of expiry and credit card number which it checks from another MySQL table created for the purpose of this project, verifies that the user is a registered client, checks the amount present in the bank account, and if sufficient funds are available it produces a bill and makes the needed changes to the bank and the stock table. 
  
Python Libraries Used
•	Tkinter : for the GUI
•	mysql.connector : for managing the records

Software Requirements:
●	Windows 7 or 10
●	Python 3.7 or above
●	My SQL 5.5 or above

MySQL TABLES
 

<img src="relative/path/in/repository/to/image.svg" width="128"/>




OUTPUT
1)	The order taking entry box
 

2)	Error message box
 



3)	Banking entry box
 
4)	Banking error message
 
5)	Bill after successful transfer
 

