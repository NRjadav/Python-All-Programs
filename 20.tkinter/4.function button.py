
import tkinter

screen=tkinter.Tk()
screen.geometry("500x500")

def myfun():
    print("this is my fun")

btn=tkinter.Button(screen,text="click here",background="black",foreground="white",height=3,width=10,font=('arial',
26,'bold'),
            activebackground="blue",activeforeground="white",command=myfun)    

btn.place(x=20,y=20)

screen.mainloop()