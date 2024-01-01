#program to display calender
import calendar

year=int(input("enter year: "))
month=int(input("enter month (1-12): "))

cal=calendar.month(year,month)
print(cal)




#complete year---------
year1=int(input("enter year: "))
m=[1,2,3,4,5,6,7,8,9,10,11,12]
for i in m:
    cal=calendar.month(year1,i)
    print(cal)