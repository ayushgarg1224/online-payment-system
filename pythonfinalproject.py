from tkinter import *
window = Tk()
window.title("Watches forever")
window.geometry("1000x1000")
from tkinter import messagebox
import mysql.connector as sql
connection = sql.connect(host = "localhost",user = "root",passwd = "Ishayush0924")
cur = connection.cursor()
#-------------------------------------------------designing tables---------------------------------
cur.execute("create database if not exists ops")
cur.execute("use ops")
cur.execute("create table if not exists items(name varchar(100) primary key , cost int, quantity int)")
cur.execute("create table if not exists bank( card_num varchar(10) primary key , CVV varchar(4) , expiry varchar(6) , amount_present int)")
try:
    cur.execute("insert into items(name,cost,quantity) values ('Casio youth',1395,8),('G-shock',3595,6),('Titan analog',1785,8)")
    cur.execute("insert into bank(card_num,CVV,expiry,amount_present) values ('123456789','123','1/21',20000),('987654321','456','2/21',12810),('234567890','789','3/21',20000)")
except:
    pass
#--------------------designing a window for the entry of the product -------------------
l1 = Label(window,text = "Please enter the product you wish to purchase:",font = ("Arial Bold",12)).grid(row = 1 , column = 0)
l2 = Label(window,text = "Please enter the quantity of the product you wish to purchase:",font = ("Arial Bold",12)).grid(row = 2 , column = 0)
product_nm = StringVar()
entry = Entry(window, text = product_nm , font = ("Arial",10))
entry.grid(row = 1 , column = 1)
qty = Spinbox(window,from_ = 1 , to = 100,width = 4)
qty.grid(row = 2 , column = 1 )
#-------------designing button functions ----------------------------------------------------
def retry():
    product_nm.set("")

def banking(cost,product,quantity,stock):
    window_2 = Tk()
    window_2.geometry("1000x1000")
    window.geometry("0x0")
    window_2.title("Card payment method")
    #-----------------------------------------------------------------------------------------------
    l1 = Label(window_2,text = "Please enter your card number",font = ("Arial Bold",12)).grid(row = 1 , column = 0)
    l2 = Label(window_2,text = "Please enter the CVV",font = ("Arial Bold",12)).grid(row = 2 , column = 0)
    l3 = Label(window_2,text = "Please enter the expiry date for the card",font = ("Arial Bold",12)).grid(row = 3 , column = 0)
    #----------------------------------------------------------------------------------------------
    
    entry1 = Entry(window_2,  font = ("Arial",10))
    entry1.grid(row = 1 , column = 1)
    #------------------------------------------------------------------------------------------------
    
    entry2 = Entry(window_2,  font = ("Arial",10))
    entry2.grid(row = 2 , column = 1)
    #-----------------------------------------------------------------------------------------------
   
    entry3 = Entry(window_2 , font = ("Arial",10))
    entry3.grid(row = 3 , column = 1)
    #----------------designing functions for buttons for the second window------------
    def retry_2():
       entry1.delete(0,"end")
       entry2.delete(0,"end")
       entry3.delete(0,"end")
    def enter_2(card,cv,exp,cost):
        cur.execute("select card_num from bank")
        result = cur.fetchall()
        if (card,) in result :
            cur.execute("select CVV,expiry from bank where card_num = %s",(card,))
            result = cur.fetchall()
            if (cv,exp) == result[0]:
                cur.execute("select amount_present from bank where card_num = %s",(card,))
                result = cur.fetchall()
                if result[0][0] >= cost :
                       window_2.geometry("1x1")
                       window_3 = Tk()
                       window_3.geometry("450x450")
                       window_3.title("Bill")
                       Label(window_3,text = "Product |").grid(row = 0 ,column = 0)
                       Label(window_3,text = "Quantity |").grid(row = 0 ,column = 1) 
                       Label(window_3,text = "Cost |").grid(row = 0 ,column = 2)
                       Label(window_3,text = "Amount left in the bank |").grid(row = 0 ,column = 3)
                       Label(window_3,text = "Quantity left in stock |").grid(row = 0 ,column = 4)
                       amount_remaining = result[0][0] - cost
                       cur.execute("update bank set amount_present = %s where card_num = %s",(amount_remaining,card))
                       connection.commit()
                       quantity_remaining = stock - int(quantity)
                       cur.execute("update items set quantity = %s where name = %s",(quantity_remaining,product))
                       connection.commit()
                       Label(window_3,text = product ).grid(row = 1 ,column = 0)
                       Label(window_3,text = quantity ).grid(row = 1,column = 1)
                       Label(window_3,text = str(cost)).grid(row = 1 ,column = 2)
                       Label(window_3,text = str(amount_remaining)).grid(row = 1 ,column = 3)
                       Label(window_3,text = str(quantity_remaining)).grid(row = 1 ,column = 4)
                        
                else :
                       messagebox.showinfo("oops","The funds in the bank are insufficient for this purchase")
                       window.geometry("350x350")
            else:
                messagebox.showinfo("oops","The card details are invalid")
        else :
            messagebox.showinfo("oops","The card details are invalid")
    #------------------------adding buttons the second window-----------------------------
    btn_retry_2 = Button(window_2,text = "RETRY" , command = retry_2).grid(row = 6 , column = 5)
    btn_enter_2 = Button(window_2,text = "ENTER" , command = lambda : enter_2(entry1.get(),entry2.get(),entry3.get(),cost)).grid(row = 6 , column = 2) 
   
def enter(product,quantity):
    qry = "select name from items "
    cur.execute(qry)
    result = cur.fetchall()
    if (product,) in result :
        cur.execute("select quantity,cost from items where name = %s",(product,))
        result = cur.fetchall()
        if int(result[0][0]) >= int(quantity) :
            cost = (int(quantity)*result[0][1])
            banking(cost,product,quantity,int(result[0][0]))
        else:
            messagebox.showinfo("Oops","We do not have that many in stock")
    else :
        messagebox.showinfo("Oops","We do not have that product in stock")
#---------------------------------------------designing buttons----------------------------------
btn_retry = Button(window,text = "RETRY",font = ("Arial Bold",10),command = retry)
btn_enter = Button(window,text = "ENTER" , font = ("Arial Bold",10),command = lambda :enter(product_nm.get(),qty.get()))
btn_retry.grid(row = 3 , column = 1 )
btn_enter.grid(row = 3 , column = 0 )
