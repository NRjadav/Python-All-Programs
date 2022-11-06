
try:
    num1=int(input("Enter a number: "))
    num2=int(input("Enter a number: "))
    print(num1/num2)
    
except ValueError:
    print("int number required")

except ZeroDivisionError:
    print("cannot be divide by zero")        