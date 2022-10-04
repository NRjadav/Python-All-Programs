
# remove duplicate elements from the list
# find unique element from the list

l1=["java","android","java","php"]

l2=[]

for i in l1:
    if i not in l2:
        l2.append(i)

print(l2)        

