
import random

l1=[]

num=random.randint(1,100)

for i in range(1,13):
    num=random.randint(1,100)
    l1.append(num)
print(l1)

for i in range(1,13):
    for i in range(1,2):
        computer=int(input("Enter a number: "))
        l1.remove(computer)
        
    print(l1)

    for i in range(1,2):
        player=int(input("Enter a number: "))
        l1.remove(player)
    print(l1)    