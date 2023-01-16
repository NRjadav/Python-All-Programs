
import tkinter
from tkinter import ttk

N=tkinter.Tk()
N.title("MY APP")
N.geometry("200x200")


M=ttk.Combobox(N,background="black",foreground="white",font=('arial',12,'bold'))
M['state']="readonly"
M['values']=("nilesh","jaydip","durgesh","ravi")
M.current(0)
M.place(x=10,y=20)



N.mainloop()
