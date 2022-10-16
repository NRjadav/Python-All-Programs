
from re import sub
from secrets import choice


def menu():
    menu_display="""
                                 MANU

                        press 1 for addition
                        press 2 for substriction
                        press 3 for multipication
                        press 4 for division   
    
    """
 
    print(menu_display)
    choice=int(input("Enter your choice : "))
    if choice==1:
        addition()
    elif choice==2:
        sub()
    elif choice==3:
        maltipication()
    elif choice==4:
        division()
    else:
        pass    

def addition():
    num1=int(input("Enter number 1 : "))
    num2=int(input("Enter number 2 : "))

    ans=num1+num2
    print(ans)

def sub():
    num1=int(input("Enter number 1 : "))
    num2=int(input("Enter number 2 : "))

    ans=num1-num2
    print(ans)

def maltipication():
    num1=int(input("Enter number 1 : "))
    num2=int(input("Enter number 2 : "))

    ans=num1*num2
    print(ans)

def division():
    num1=int(input("Enter number 1 : "))
    num2=int(input("Enter number 2 : "))

    ans=num1/num2
    print(ans)
menu()    