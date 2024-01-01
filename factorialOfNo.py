num=int(input("enter the number to find factorial: "))

if num<0:
    print("cannot find for -ve values")
elif num==0:
    print("1")
else:
    fact=1
    for i in range(1,num+1):
        fact=fact*i
    print(fact)

#using recursion
num=int(input("enter the number to find factorial: "))
def fact(num):
    if num==0:
        return 1
    fact1=num*fact(num-1)
    return fact1

print(fact(num))
