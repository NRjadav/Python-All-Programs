
import tkinter

N=tkinter.Tk()
N.title("My App")
N.geometry("500x500")

name_var=tkinter.StringVar()
age_var=tkinter.StringVar()
sub=tkinter.StringVar()
dto=tkinter.StringVar()
add=tkinter.StringVar()
phone=tkinter.StringVar()

def fun():
    name=name_var.get()
    age=age_var.get()
    subject=sub.get()
    date=dto.get()
    addre=add.get()
    phonen=phone.get()
    print(name)
    print(age)
    print(subject)
    print(date)
    print(addre)
    print(phonen)

lbl=tkinter.Label(N,text="STUDENT INTRODUCTION",font=('arial',12,'bold'))
lbl.place(x=150,y=10)

lbl=tkinter.Label(N,text="NAME",font=('arial',12,'bold'))
lbl.place(x=10,y=50)

username=tkinter.Entry(N,background="white",font=('arial',12,'bold'),textvariable=name_var)
username.place(x=150,y=50)

lbl=tkinter.Label(N,text="AGE",font=('arial',12,'bold'))
lbl.place(x=10,y=90)

age=tkinter.Entry(N,background="white",font=('arial',12,'bold'),textvariable=age_var)
age.place(x=150,y=90)

lbl=tkinter.Label(N,text="SUBJECT",font=('arial',12,'bold'))
lbl.place(x=10,y=130)

subject=tkinter.Entry(N,background="white",font=('arial',12,'bold'),textvariable=sub)
subject.place(x=150,y=130)

lbl=tkinter.Label(N,text="DATE OF BIRTH",font=('arial',12,'bold'))
lbl.place(x=10,y=170)

dto=tkinter.Entry(N,background="white",font=('arial',12,'bold'),textvariable=dto)
dto.place(x=150,y=170)

lbl=tkinter.Label(N,text="ADDRESS",font=('arial',12,'bold'))
lbl.place(x=10,y=210)

address=tkinter.Entry(N,background="white",font=('arial',12,'bold'),textvariable=add)
address.place(x=150,y=210)

lbl=tkinter.Label(N,text="PHONE NUMBER",font=('arial',12,'bold'))
lbl.place(x=10,y=250)

phone_number=tkinter.Entry(N,background="white",font=('arial',12,'bold'),textvariable=phone)
phone_number.place(x=150,y=250)


btn=tkinter.Button(N,text="SUBMIT",background="red",foreground="black",command=fun)
btn.place(x=200,y=300)

N.mainloop()