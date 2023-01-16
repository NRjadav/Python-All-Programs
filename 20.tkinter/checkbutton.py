
import tkinter

N=tkinter.Tk()
N.title("MY APP")
N.geometry("200x200")

checkbutton1=tkinter.IntVar()
checkbutton2=tkinter.IntVar()

def fun():
    male=checkbutton1.get()
    female=checkbutton2.get()
    print(male)
    print(female)



btn=tkinter.Checkbutton(N,text="male",background="white",foreground="black",activebackground="green",activeforeground="blue",
                        font=('arial',12,'bold'),onvalue=1,offvalue=0,variable=checkbutton1)
btn.place(x=10,y=10)                        

btn=tkinter.Checkbutton(N,text="female",background="white",foreground="black",activebackground="green",activeforeground="blue",
                        font=('arial',12,'bold'),onvalue=1,offvalue=0,variable=checkbutton2)
btn.place(x=10,y=40)

btn=tkinter.Button(N,text="get data",background="white",foreground="black",activebackground="green",activeforeground="blue",
                        font=('arial',12,'bold'),command=fun)
btn.place(x=30,y=80)


N.mainloop()