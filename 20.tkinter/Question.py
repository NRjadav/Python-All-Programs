
import tkinter

N=tkinter.Tk()
N.title("QUESTION PAPER")
N.geometry("300x300")

p=tkinter.IntVar()

def fun():
    if p.get()==1:
        print("python")
    elif p.get()==2:
        print("java")
    elif p.get()==3:
        print("php")
    else:
        print("cc++")
    


lbl=tkinter.Label(N,text="STD 12",background="white",foreground="black",font=('arial',30,'bold'))
lbl.place(x=30,y=10)

lbl=tkinter.Label(N,text=" Q1 : best progaramming langaue? ")
lbl.place(x=10,y=50)
btn=tkinter.Radiobutton(N,text="python",value=1,variable=p)
btn.place(x=20,y=100)
btn=tkinter.Radiobutton(N,text="java",value=2,variable=p)
btn.place(x=20,y=120)
btn=tkinter.Radiobutton(N,text="php",value=3,variable=p)
btn.place(x=20,y=140)
btn=tkinter.Radiobutton(N,text="cc++",value=4,variable=p)
btn.place(x=20,y=160)
btn=tkinter.Button(N,text="ANS",command=fun)
btn.place(x=30,y=200)



N.mainloop()




