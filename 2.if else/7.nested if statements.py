"""

nested if statements syntax:

if condition:
    statements
    if condition:
        statements
    else:
        statements

elif condition:
    statements
    if condition:
        statements 
    else:
        statements 

"""

ind=int(input("enter score:"))
aus=int(input("enter score:"))
pak=int(input("enter score:"))

if aus>pak:
    if aus>ind:
        print("AUS WON THE MATCH")
    else:
        print("IND WON THE MATCH")
else:
    if pak>ind:
        print("PAK WON THE MATCH")
    else:
        print("IND WON THE MATCH")                






