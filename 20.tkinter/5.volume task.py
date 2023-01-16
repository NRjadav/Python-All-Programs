
import tkinter

screen=tkinter.Tk()
screen.geometry("500x500")

lbl=tkinter.Label(screen,text="volume up-down button",font=('arial',20,'bold'))
lbl.place(x=50,y=10)

a=0
def volume_up():
    global a
    a=a+1
    print(a)    

def volume_low():
    global a
    if 0<a:
        
        
        a=a-1
        print(a)

btn1=tkinter.Button(screen,text="+ Button",background="black",foreground="white",font=('arial',5,'bold'),
                    height=3,width=10,activebackground="blue",activeforeground="red",command=volume_up)
btn1.place(x=50,y=100)

btn2=tkinter.Button(screen,text="- Button",background="black",foreground="white",font=('arial',5,'bold'),
                    height=3,width=10,activebackground="blue",activeforeground="red",command=volume_low)                    
btn2.place(x=50,y=150)
screen.mainloop()



