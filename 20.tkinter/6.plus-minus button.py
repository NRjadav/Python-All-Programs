
from tkinter import *

screen=Tk()
screen.geometry("500x500")

score=IntVar()
currentscore=0
score.set(currentscore)
def myfunplus():
    global score,currentscore
    currentscore+=1
    score.set(currentscore)

def myfunminius():
    global score,currentscore
    currentscore-=1
    score.set(currentscore)

btnplus=Button(screen,text="+",background="blue",foreground="white",font=('Arial',26,'bold'),command=myfunplus)
btnplus.place(x=10,y=10)

btndisplay=Button(screen,textvariable=score,background="white",foreground="blue",font=('Arial',26,'bold'))
btndisplay.place(x=80,y=10)

btnminus=Button(screen,text="-",background="blue",foreground="white",font=('Arial',26,'bold'),command=myfunminius)
btnminus.place(x=160,y=10)

screen.mainloop()


