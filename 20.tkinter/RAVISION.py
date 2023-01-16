
# import tkinter

# tk=tkinter.Tk()

# tk.title("my app")
# tk.geometry("300x300")

# lbl=tkinter.Label(tk,text="WELCOME TO TKINTER",font=('arial',12,'bold'))
# lbl.place(x=50,y=10)

# def myfun():
#     print(1)
# def myfun1():
#     print(2)

# btn=tkinter.Button(tk,text="click me",background="black",foreground="white",font=('arial',12,'bold'))
# btn.place(x=10,y=40)

# btn=tkinter.Radiobutton(tk,text="python",font=('arial',12,'bold'),value=1,command=myfun)
# btn.place(x=10,y=40)

# btn=tkinter.Radiobutton(tk,text="java",font=('arial',12,'bold'),value=2,command=myfun1)
# btn.place(x=10,y=80)

# lbl=tkinter.Label(tk,text="name",font=('arial',12,'bold'))
# lbl.place(x=10,y=40)
# ent=tkinter.Entry(tk,font=('arial',12,'bold'))
# ent.place(x=100,y=40)
# tk.mainloop()

import tkinter

N=tkinter.Tk()
N.title("My App")
N.geometry("300x300")

# lbl=tkinter.Label(N,text="Welcome",font=('arial',12,'bold'))
# lbl.place(x=10,y=10)

# btn=tkinter.Button(N,text="Tkinter",font=('arial',12,'bold'))
# btn.place(x=10,y=40)

# btn=tkinter.Radiobutton(N,text='python',font=('arial',12,'bold'),value=1)
# btn.place(x=10,y=10)
# btn=tkinter.Radiobutton(N,text='java',font=('arial',12,'bold'),value=2)
# btn.place(x=10,y=30)

lbl=tkinter.Label(N,text="name",font=('arial',12,'bold'))
lbl.place(x=10,y=10)
ent=tkinter.Entry(N,font=('arial',12,'bold'))
ent.place(x=60,y=10)

N.mainloop()




























