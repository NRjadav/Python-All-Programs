
import calendar

strat=int(input("enter a year:"))
end=int(input("enter a year:"))



for n in range(strat,end):
    for i in range(1,13):
        print(calendar.month(n,i))


