
import random

computer = random.randint(1,100)
# print(computer)

status=True


while status:
    for i in range(1,11):
        user =int(input("Enter number :"))

        if user>computer:
            print("HINT guess lower number")
        elif user<computer:
            print("HINT guess upper number")
        else:
            print("YOU GOT IT")
            break
        status=False
    else:
        print("game ovar")
        
        
                
   
        