
l1=[]

f = open("example.txt","a")

for i in range(1,6):
    name=input("Enter name: ")
    l1.append(name)


f.write("\n"+str(l1))
f.close()

