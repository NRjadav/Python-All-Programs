
gujrati=int(input("enter your marks:"))
english=int(input("enter your marks:"))
maths=int(input("enter your marks:"))
economics=int(input("enter your marks:"))
history=int(input("enter your marks:"))

total=gujrati+english+maths+economics+history
print(total)

persentage=total/5
print(persentage)

if persentage>=90 and persentage<=100:
    print("gread A+")

elif persentage>=80 and persentage<90:
    print("gread A")

elif persentage>=70 and persentage<80:
    print("gread B+")

elif persentage>=60 and persentage<70:    
    print("gread B")

elif persentage>=50 and persentage<60:
    print("gread C")

elif persentage>=35 and persentage<50:
    print("gread D")

else:
    print("fail")         











