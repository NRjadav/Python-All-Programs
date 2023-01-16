
from tkinter import *
import pymysql
import my_db_connection

my_db_connection.myconnection()
screen=Tk()
screen.geometry("500x500")


e1_var=StringVar()
e2_var=StringVar()
e3_var=StringVar()
lbl_massage=StringVar()


# ----------------------logic-------------------------------

mydb=pymysql.connect(host="localhost",user="root",password="",database="12_sep_python")
mycursor=mydb.cursor()

def adddata():
    query="insert into student (firstname,lastname,subject) values ('%s','%s','%s')"
    values=(e1_var.get(),e2_var.get(),e3_var.get())

    mycursor.execute(query%values)
    mydb.commit()
    lbl_massage.set("successfully data inserted !!!")

def updateData():
    query="UPDATE student SET  lastname = '%s' , subject ='%s' WHERE firstname = '%s' "
    values=(e2_var.get(),e3_var.get(),e1_var.get())

    mycursor.execute(query%values)
    mydb.commit()
    lbl_massage.set("successfully data updated !!!")

def deleteData():
    query="Delete from student where firstname='%s' "
    values=(e1_var.get())

    mycursor.execute(query%values)
    mydb.commit()
    lbl_massage.set("successfully data deleted !!!")




# =====================logic===================

# =====================designing===================

lbl=Label(screen,text="Enter your firstname : ",font=('arial',12,'bold'))
lbl.place(x=10,y=10)

e1=Entry(screen,textvariable=e1_var)
e1.place(x=200,y=10)

lbl=Label(screen,text="Enter your lastname : ",font=('arial',12,'bold'))
lbl.place(x=10,y=60)

e1=Entry(screen,textvariable=e2_var)
e1.place(x=200,y=60)

lbl=Label(screen,text="Enter your subject : ",font=('arial',12,'bold'))
lbl.place(x=10,y=120)

e1=Entry(screen,textvariable=e3_var)
e1.place(x=200,y=120)

btn=Button(screen,text="SAVE",width=5,command=adddata)
btn.place(x=20,y=160)

lbl=Label(screen,textvariable=lbl_massage)
lbl.place(x=100,y=250)

btn_update=Button(screen,text="UPDATE",width=5,command=updateData)
btn_update.place(x=100,y=160)

btn_delete=Button(screen,text="DELETE",width=5,command=deleteData)
btn_delete.place(x=160,y=160)

# ================designing============

screen.mainloop()



