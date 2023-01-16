
import tkinter

N=tkinter.Tk()
N.title("My App")
N.geometry("500x500")

lbl=tkinter.Label(N,text="Welcome to tkinter",font=('arial',12,'bold'))
lbl.place(x=10,y=20)

btn=tkinter.Button(N,text="click here",background="black",foreground="white")
btn.place(x=10,y=100)

N.mainloop()