#program to check leap year
#year=365days
#leapYear=366days --once in four year
year=int(input("enter the year: "))

if(year %400==0) and (year % 100==0):
    print(year," is leap year")
elif(year %4 ==0) and (year %100 !=0):
    print(year," is a leap year")
else:
    print(year," is not a leap year")

