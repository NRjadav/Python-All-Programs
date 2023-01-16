
import tkinter
from tkinter import messagebox

N=tkinter.Tk()
N.title("MY APP")
N.geometry("300x300")

def fun():
    if var.get()=="":
        messagebox.showwarning("warning","empty box")
    else:
        messagebox.showinfo("success",var.get())    

var=tkinter.StringVar()
ent=tkinter.Entry(N,textvariable=var)
ent.place(x=20,y=20)

btn=tkinter.Button(N,text="get",command=fun)
btn.place(x=30,y=50)

N.mainloop()

