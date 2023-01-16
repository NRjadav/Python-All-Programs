
import tkinter
import datetime

screen=tkinter.Tk()
screen.title("my app")
screen.geometry("500x500")

n=tkinter.StringVar()
g=tkinter.StringVar()
e=tkinter.StringVar()
c=tkinter.StringVar()
vn=tkinter.StringVar()
vd=tkinter.StringVar()

def fun():
    d=datetime.datetime.now()
    # print(d)

    
    n1=n.get()
    g1=g.get()
    e1=e.get()
    c1=c.get()
    vn1=vn.get()
    vd1=vd.get()
    # print(n1)
    # print(g1)
    # print(e1)
    # print(c1)
    # print(vn1)
    # print(vd1)

    f=open("vaccination.txt","w")
    f.write(n.get())
    f.write("\n")
    f.write(g.get())
    f.write("\n")
    f.write(e.get())
    f.write("\n")
    f.write(c.get())
    f.write("\n")
    f.write(vn.get())
    f.write("\n") 
    f.write(vd.get())

    print(n1)
    print(g1)
    print(e1)
    print(c1)
    print(vn1)
    print(vd1)
    
    f.close()

    

name=tkinter.Label(screen,text="NAME",font=('arial',16,'bold'))
name.place(x=10,y=10)
name1=tkinter.Entry(screen,background="white",font=('arial',16,'bold'),textvariable=n)
name1.place(x=250,y=10)

gender=tkinter.Label(screen,text="GENDER",font=('arial',16,'bold'))
gender.place(x=10,y=50)
gender1=tkinter.Entry(screen,background="white",font=('arial',16,'bold'),textvariable=g)
gender1.place(x=250,y=50)

email=tkinter.Label(screen,text="EMAIL",font=('arial',16,'bold'))
email.place(x=10,y=90)
email1=tkinter.Entry(screen,background="white",font=('arial',16,'bold'),textvariable=e)
email1.place(x=250,y=90)

contact=tkinter.Label(screen,text="CONTACT",font=('arial',16,'bold'))
contact.place(x=10,y=130)
contact1=tkinter.Entry(screen,background="white",font=('arial',16,'bold'),textvariable=c)
contact1.place(x=250,y=130)

v_name=tkinter.Label(screen,text="VACCINE NAME",font=('arial',16,'bold'))
v_name.place(x=10,y=170)
v_name1=tkinter.Entry(screen,background="white",font=('arial',16,'bold'),textvariable=vn)
v_name1.place(x=250,y=170)

v_doze=tkinter.Label(screen,text="VACCINETION DOZE",font=('arial',16,'bold'))
v_doze.place(x=10,y=210)
v_doze1=tkinter.Entry(screen,background="white",font=('arial',16,'bold'),textvariable=vd)
v_doze1.place(x=250,y=210)

btn=tkinter.Button(screen,text="SUBMIT",command=fun)
btn.place(x=250,y=250)

screen.mainloop()