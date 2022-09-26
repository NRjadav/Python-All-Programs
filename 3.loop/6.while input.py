
status=True

while status:
    num=int(input("enter a number:"))
    if num>=50:
        print("above 50")
    else:
        print("below 50")

    choice=input("'y' for yes 'n' for no")

    if choice=='y':
        status=True
    else:
        status=False        






