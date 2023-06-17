
# print("hello")
# print("nilesh")

"""sjjkkl
jklsljlk
kjksj"""

# a=10

# print(a)


# a=10
# b=10.10
# c="nilesh"
# d=True
# e=None

# print(type(a))
# print(type(b))
# print(type(c))
# print(type(d))
# print(type(e))

# print(a)
# print(b)
# print(c)
# print(d)
# print(e)

# a=int(input("Enter A Number : "))
# print(a)
# print(type(a))

# name="nilesh"
# age=22

# print(f"my name is {name} and my age is {age}")
# output = my name is nilesh and my age is 22

# output = nilesh 22

# print(name,age)
# print(name,end=" ")
# print(age)


# _a1_=10


# sum=0

# for i in range(1,11):
#     sum+=i
# print(sum)    

# odd=0

# for i in range(1,12):
#     if i%2==0:
#         pass
#     else:
#         odd+=1
# print(odd)


# for i in range(1,11):
#     for n in range(1,11):
#         print(f"{n}*{i}={n*i}")


# evan=0
# odd=0

# for i in range(1,11):
#     if i%2==0:
#         evan+=1
#     else:
#         odd+=1 

# print(evan)
# print(odd)

# num=1234567890

# num1=str(num)
# count=0
# for i in num1:
#     count+=1
# print(count)
    

# num="nil"

# num1=""

# for i in num: #
#     num1=i+num1


# if num==num1:
#     print("p")
# else:
#     print("n")


# num = input("Enter a number: ")

# if num == num[::-1]:
#     print("The number is a palindrome!")
# else:
#     print("The number is not a palindrome!")


# a=4*4*4
# b=7*7*7

# print(a+b)


# num=int(input("Enter A Number : "))
# sum=0
# temp=num

# while temp>0:
#     digit=temp%10
#     sum=sum+digit**3
#     temp=temp//10

# if num==sum:
#     print("armstonge number")

# else:
#     print("not a armstodg number") 



# start=int(input("Enter A Number : "))
# end=int(input("Enter A Number : "))



# for i in range(start,end):
#     for n in range(1,11):
#         print(f"{i}*{n}={n*i}")
#     print("\n")


# start=int(input("Enter A Number : "))
# end=int(input("Enter A Number : "))
# sum=0

# for i in range(start,end):
#     sum+=i
# print(sum)


# l1=[1,2,3,4,5,6,7]
# l1=[1,2,1.2,1.3,"nilesh",True,None]

# l1=[1,2,3,4,5,6,"nilesh",True]


# print(l1[-:1])
# print(l1[2:5:2])

# print(l1[::])

#  2 1

# l1=[10,2,4,19,57,8,3,6,7,8,1]  
# print(len(l1))

# print(sum(l1))

# print(max(l1))

# print(min(l1))

# print(l1[1][0])

# l1.sort(reverse=True)

# l1.append(90)
# l1.extend([20,31,90])
# l1.insert(1,11)
# print(l1)


# name='nilesh'
# name1="nilesh"
# name2="""nilesh
#     nilesh
# nilesh"""


# print(name)
# print(name1)
# print(name2)

# name="jadav nilesh jadav"

# print(len(name))

# print(name.capitalize())

# print(name.upper())

# print(name.lower())

# print(name.isupper())

# print(name.islower())

# print(name.find("J"))

# print(name.endswith("av"))

# print(name.replace("jadav","python"))

# print(name.split())


# name="nilesh"
# age=24

# print(f"my name is {name} and my age is {age}")
# output :  my name is nilesh and my age is 23


#================================ list===========================================
# 


# l1=[1,22,33,44,2,3,4,55,6,7,8,9,10]
# l1=[1,2,"nilesh",1.3,True,None,True]

# print(l1[2:4])

# print(l1[-1])

# print(len(l1))

# print(sum(l1))

# print(max(l1))

# print(min(l1))

# l1.sort()
# l1.reverse()

# l1.append(23)

# l1.extend([1,2,3,4,5,6])

# l1.insert(1,23)
# l1=[1,22,33,44,2,3,4,55,6,7,8,9,10]
# l1.pop(1)
# l1.pop()
# l1.clear()
# l1.remove(44)
# del l1
# l2=l1.copy()
# l3=l1.copy()
# print(l2)
# print(l3)
# ==================================

# l1= ["Apple", "Banana", "Car", "Dolphin" ]

# for i in l1:
#     for n in i:
#         print(n)
#     print("/////")
    
# name="nilesh12345"
# sum=0

# for i in name:
#     sum=sum+1

# print(sum)    
    
    

    # =================================================
# month=input("Enter  A Month : ")

# if month=="jan" or month=="mar":
#     print("31")
# elif month=="feb":
#     print("28")
# else:
#     print("30")    


# input password from user
# password = input()
 
# set up flags for each criteria
# of a valid password
# has_valid_length = False
# has_lower_case = False
# has_upper_case = False
# has_digits = False
# has_special_characters = False
 
 
# first verify if the length of password is
# higher or equal to 8 and lower or equal to 16
# if (len(password) >= 8) and (len(password)<=16):
 
#     has_valid_length = True
 
    # iterate through each characters
    # of the password
    # for i in password:
 
        # check if there are lowercase alphabets
        # if (i.islower()):
        #         has_lower_case = True                   
 
        # check if there are uppercase alphabets
        # if (i.isupper()):
        #         has_upper_case = True                   
 
        # check if the password has digits
        # if (i.isdigit()):
        #         has_digits = True                       
 
        # check if the password has special characters
#         if(i=="@" or i=="$" or i=="_"or i=="#" or i=="^" or i=="&" or i=="*"):
#                 has_special_characters = True           
 
 
# if (has_valid_length==True and has_lower_case ==True and has_upper_case == True and has_digits == True and has_special_characters == True):
#     print("Valid Password")
# else:
#         print("Invalid Password")

# ============================


# a=[1,2,3,4,5,6,7,8]

# print(a)


# output: [1,2,3,[1,2,3,4],4,5,6,[1,2,3,4,5],7,8,9,10,[1,2,3,4,3,2,1]]

# a.insert(3,[1,2,3,4])
# a.insert(7,[1,2,3,4,5])
# a.append(9)
# a.append(10)
# a.append([1,2,3,4,3,2,1])
# print(a)


# a=[1,2,3,4,5,6,7,8,[1,2,3,4,5,6]]

# a.pop(-1)

# a.remove(1)
# a.remove(2)
# a.clear()


# del a


# print(a)

# l1=["python","django","java"]

# for i in l1: #  python
#     for n in i: # p y t h o n  d j a n g o
#         print(n,end=" ") # pythondjango



# d1={
#     "name":"nilesh",
#     "age":23,
#     "subject":"python"

# }

# print(d1)
# print(type(d1))

# print(d1.keys())
# print(d1.values())
# print(d1.items())
# d1.update({"class":1})
# print(d1)

# ===============

# if condition:
#     code
# elif codition:
#     code
# elif condition:
#     code    
# else:
#     code    

# if condition:
#     if condition:
#         code


# a=111

# if a==11:
#     print("yes")

# elif a<20:
#     print("yes1")

# else:
#     print("no")

# a=int(input("Enter A number : "))

# if a%2==0:
#     print("evan  number")
# else:
#     print("odd number")     

# a=10

# if a==11:
#     if a<10:
#         print("yes") 
#     else:
#       print("no1")


# else:
#     print("no")        



# password=input("enter a password : ")

# len1=False
# up1=False
# lo=False
# di=False

# if len(password)>=8:
#     len1=True
#     for i in password:
#         if i.isupper():
#             up1=True
#         if i.islower():
#             lo=True
#         if i.isdigit():
#             di=True


# if len1==True and up1==True and lo==True and di==True:
#     print("Valid Password")
# else:
#     print("Envalid Password")
               
# n=12345
# a=str(n)
# c=0
# for i in a:
#     c+=1
# print(c)    
# e=0
# o=0

# for i in range(1,11):
#     if i%2==0:
#         e+=i # 2,4,6,8,10
#     else:
#         o+=i # 1,3,5,7,9  
# print(e)
# print(o)          

# num=1234567

# num=str(num)

# a=int(num[2])
# b=int(num[-1])
# print(len(num))
# print(a+b)


# a=[1,2,3,4,5,6]

# a[0],a[-1]=a[-1],a[0]

# print(a)




